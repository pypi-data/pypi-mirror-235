from promptflow.azure import PFClient
import json
from datetime import datetime
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel.orchestration.sk_context import SKContext


from flow_agent_package.tools.contracts import AgentSkillConfiguration, FlowSkillConfiguration
from flow_agent_package.tools.flow_manager import FlowManager
from flow_agent_package.tools.skills.agent_skill import AgentSkill


class FlowSkill(AgentSkill):
    """
        Skill that executes a PF (a sub-flow) in the current environment. Using a flow name, stores information about the flow, 
        which is used by the agent when selecting a skill to execute. If chosen, the flow skill downloads the flow's files, gets
        connections, and executes the sub-flow using a local PF Client.
    """
    def __init__(self, config: FlowSkillConfiguration, pf: PFClient, subscription_id, resource_group, workspace_name, memory_manager):
        super().__init__(config, memory_manager)
        self.flow_manager = FlowManager(pf, config.flow_name, subscription_id, resource_group, workspace_name)        
        self.function_description = self.init_description(self.flow_manager.flow_json, config)
  
    def init_description(self, flow_json, config):
        """Coalesce provided skill description and flow's description"""
        config_desc = config.description
        # In case of default desc, use tool description
        # TODO: default to config description first?
        if flow_json.get("description") == "Template Standard Flow" or flow_json.get("description") == "Template Chat Flow":
            return config_desc
        return flow_json.get("description", config_desc)

    def get_langchain_tool_description(self):
        """Get description of skill for use in langchain tool"""
        return self.function_description + self.flow_manager.get_input_descriptions()

    
    def to_function_definition(self):
        return {
            "name": self.flow_manager.flow_json["flowName"].replace(" ", "_"),
            "description": self.function_description,
            "parameters":{
                "type": "object",
                "properties": self.flow_manager.input_config
            }
        }

    def to_langchain_function(self):
        # String -> string function for langchain
        def run_str(query):
            result = self.execute(json.loads(query))
            return result
        
        return run_str

    def to_sk_function(self):
        # Function of SK. Takes in string of a dictionary of inputs
        @sk_function(
            description=self.function_description,
            name=self.name
        )
        def sk_execute_func(query: str) -> str:
            result = self.execute(json.loads(query))
            return result
        return sk_execute_func

    def to_sk_function_dynamic(self):
        # Function for SK. Takes in Context with vars populated
        def sk_execute_func(context: SKContext) -> str:
            
            input_names = list(self.flow_manager.input_config.keys())
            input_json = {}
            for name in input_names:
                if name == self.changed_input:
                    sk_name = "input"
                else:
                    sk_name = name
                
                input_json[name] = context[sk_name]
                
            
            print(input_json)
            result = self.execute(input_json)
            return result
        og_func = sk_execute_func
        input_used = False

        # Add decorators for each input required
        for input_name, input_metadata in self.flow_manager.input_config.items():
            if input_used:
                name = input_name
                description = input_metadata.get("description", "")
                context_decorator = sk_function_context_parameter(name=name, description=description)
                og_func = context_decorator(og_func)
            else:
                name = "input"
                description = input_metadata.get("description", input_name)
                main_wrap = sk_function(description=self.function_description, name=self.name, input_description=description)
                og_func = main_wrap(og_func)
                self.changed_input = input_name
                input_used = True
  
        return og_func

    def execute(self, inputs) -> dict:
        try:
            print("Starting to Execute Sub-flow")
            execute_start_time = datetime.now()
            
            # Set chat history for chat flow to be current agent history
            if self.flow_manager.is_chat_flow:
                inputs["chat_history"] = self.memory_manager.history

            # Run Flow Locally
            answer = self.flow_manager.execute_flow(inputs)
            print(f"Time to Prep and Execute Flow: {datetime.now() - execute_start_time}")
            return answer
        except Exception as e:
            print(f"Exception encountered: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return f"Unable to execute skill {self.name} due to exception: {str(e)}"

