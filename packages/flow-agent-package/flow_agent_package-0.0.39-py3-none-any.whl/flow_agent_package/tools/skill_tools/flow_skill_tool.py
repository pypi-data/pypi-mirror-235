from promptflow import tool
from flow_agent_package.tools.contracts import FlowSkillConfiguration

@tool
def flow_skill(name: str, description: str, flow_id: str, return_direct: bool):
  """Creates a FlowSkillConfiguration for use in a Flow Agent.""" 
  config = FlowSkillConfiguration(name=name, description=description, flow_name=flow_id, return_direct=return_direct)
  return config
