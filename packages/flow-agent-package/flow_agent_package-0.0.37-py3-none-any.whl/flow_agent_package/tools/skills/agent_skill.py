
from abc import abstractmethod
from flow_agent_package.tools.contracts import AgentSkillConfiguration

class AgentSkill:
    """
        Skill used in Flow Agent. Provides a means of representing each skill's action
        (i.e. executing a flow, retrieving documents from index, calling API) in a
        way that can be used by the agent's arbitration method (i.e functions for OpenAI,
        semantic kernel native fuctions) so the agent can pick and execute them.
    """
    
    def __init__(self, config: AgentSkillConfiguration, memory_manager):
        self.name = config.name
        self.tool_description = config.description
        self.return_direct = config.return_direct
        self.memory_manager = memory_manager
    
    @abstractmethod
    def to_function_definition(self):
        """Represent the skill as a function definition"""

    @abstractmethod
    def to_langchain_function(self):
        """Represent the skill as a function for langchain agent"""

    @abstractmethod
    def to_sk_function(self):
        """Represent the skill as a sk function"""

    @abstractmethod
    def to_sk_function_dynamic(self):
        """Represent the skill as a sk function with dynamic input decorators"""

    @abstractmethod
    def execute(self, inputs) -> dict:
        """Execute the Skill"""