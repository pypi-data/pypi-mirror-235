
from flow_agent_package.tools.skills.agent_skill import AgentSkill
from flow_agent_package.tools.contracts import MIRSkillConfiguration
from promptflow.entities import CustomConnection as LocalCustomConnection
from semantic_kernel.skill_definition import sk_function
import requests 
import urllib
import openai
import json
from azure.ai.ml import MLClient

from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel.orchestration.sk_context import SKContext

class MIRSkill(AgentSkill):

    def __init__(self, config: MIRSkillConfiguration, memory_manager, ml_client: MLClient):
        super().__init__(config, memory_manager)
        self.endpoint_name = config.endpoint_name
        self.deployment_name = config.deployment_name
        self.input_config = config.input_config
        self.ml_client = ml_client
        self.output_path = config.output_path


    def to_function_definition(self):
        """Represent the skill as a function definition"""
        return {
            "name": self.name,
            "description": self.tool_description,
            "parameters":{
                "type": "object",
                "properties": self.input_config
            }
        }
    
    def get_input_descriptions(self):
        input_description = "The inputs to this tool, in order, are \n"
        for input_name, input_metadata in self.input_config.items():
            input_description += f"Input Name: {input_name}, Input Type: {input_metadata['type']}"
            if input_metadata.get("description"):
                input_description += f"Input Description: {input_metadata.get('description')}"
            input_description += "\n"
        return input_description

    def get_langchain_tool_description(self):    
        return self.tool_description + self.get_input_descriptions()


    def to_langchain_function(self):

        def run_str(query):
            result = self.execute(json.loads(query))
            return result
        return run_str
        
    def to_sk_function(self):
        
        # Function of SK. Takes in string of a dictionary of inputs
        @sk_function(
            description=self.tool_description,
            name=self.name
        )
        def sk_execute_func(query: str) -> str:
            result = self.execute(json.loads(query))
            return result
        return sk_execute_func

    def to_sk_function_dynamic(self):

        # Function for SK. Takes in Context with vars populated
        def sk_execute_func(context: SKContext) -> str:
            
            input_names = list(self.input_config.keys())
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
        for input_name, input_metadata in self.input_config.items():
            if input_used:
                name = input_name
                description = input_metadata.get("description", "")
                context_decorator = sk_function_context_parameter(name=name, description=description)
                og_func = context_decorator(og_func)
            else:
                name = "input"
                description = input_metadata.get("description", input_name)
                main_wrap = sk_function(description=self.tool_description, name=self.name, input_description=description)
                og_func = main_wrap(og_func)
                self.changed_input = input_name
                input_used = True
            
            
        return og_func

    def parse_output(self, response):
        json_path = self.output_path.split(".")
        current = response
        for step in json_path:
            try:
                # Handle list index values
                idx = int(step)
            except ValueError:
                # Can't parse, assume key
                idx = step
            current = current[idx]

        # After traversing path, should have answer
        return current

            

    def execute(self, inputs) -> dict:

        for ep in self.ml_client.online_endpoints.list():
            if ep.name == self.endpoint_name:
                target = ep.scoring_uri
                endpoint_key = self.ml_client.online_endpoints.get_keys(ep.name).primary_key
                found = True
                break
        
        if not found:
            raise ValueError(f"Endpoint {self.endpoint_name} not found.")
        print("Found Endpoint")
        if self.deployment_name:
            found = False

            for d in self.ml_client.online_deployments.list(ep.name):
                if d.name == self.deployment_name:
                    found = True
                    break

            if not found:
                raise ValueError(f"Deployment {self.deployment_name} not found.")  


        headers = {"Content-Type": "application/json"}
        if self.deployment_name:
            headers["azureml-model-deployment"] = self.deployment_name
        if endpoint_key:
            headers["Authorization"] = "Bearer " + endpoint_key
        else:
            # Get AzureML Token somehow
            raise Exception('PAT not supported yet!')
            # Use token in header
        
        # Validate inputs
        for input_name, value in inputs.items():
            if input_name not in self.input_config.keys():
                raise Exception(f"Incorrect inputs for MIR Tool given by LLM: {inputs}")

        body = str.encode(json.dumps(inputs))
        try:
            response = requests.post(target, data=inputs, headers=headers).json()
            print(response)
            return self.parse_output(response)
        except Exception as error:
            print("The request failed with exception " + str(error))
            raise
        
