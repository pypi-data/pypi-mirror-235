from promptflow import tool
from flow_agent_package.tools.contracts import MLIndexSkillConfiguration
import string

@tool
def mlindex_skill(name: str, description: str, asset_path: str, return_direct: bool = True):
  """Creates a MLIndexSkillConfiguration for use in a Flow Agent."""

  # if (system_prompt == "" or system_prompt == None) and not return_direct:
  #   raise Exception("System prompt must be provided if return_direct is false, as LLM cannot process raw documents")
  
  # if system_prompt != "" and system_prompt != None:
  #    vars = [tup[1] for tup in string.Formatter().parse(system_prompt) if tup[1] is not None]
  #    if "question" not in vars or "context" not in vars:
  #      raise Exception("Formatting fields 'question' and 'context' must be present in system prompt!")
  
  # MLIndex SKills must return raw docs
  config = MLIndexSkillConfiguration(name=name, description=description, index_path=asset_path, return_direct=True, system_prompt=None)
  return config