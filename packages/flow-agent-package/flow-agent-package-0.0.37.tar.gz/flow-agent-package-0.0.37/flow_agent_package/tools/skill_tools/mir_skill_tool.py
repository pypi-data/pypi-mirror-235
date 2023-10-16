from promptflow import tool
from flow_agent_package.tools.contracts import MIRSkillConfiguration
from promptflow.connections import CustomConnection
import json

input_structure_error = """
Input config structure must be as follows:
{
  "<input_name>": {
      "type": "<type>"
      "description": "<description>" (optional)
  }
}
"""

@tool
def mir_skill(name: str, description: str, mir_connection: CustomConnection, input_config: str, output_path: str, return_direct: bool = True):
  """Creates a MIRSkillConfiguration for use in a Flow Agent"""

  # Validate the connection here to fail fast
  auth_type = mir_connection.configs.get("authType")
  if auth_type == None or (auth_type != "key" and auth_type != "PAT"):
    raise Exception("CustomConnection for MIR Skill must have authType of 'key' or 'PAT' set!")

  if auth_type == "key":
    key = mir_connection.secrets.get("key")
    if key == None:
      raise Exception("CustomConnection for MIR Skill has authType of 'key' but no key is set!")

  target = mir_connection.configs.get("target")
  if target == None:
    raise Exception("CustomConnection for MIR Skill is missing target!")  

  input_json = json.loads(input_config)
  for key, value in input_json.items():
    if not isinstance(value, dict):
      raise Exception(input_structure_error)
    if value.get("type") == None:
      raise Exception(input_structure_error)
  print(f"Connection Name: {mir_connection.name}")

  # Pass only connection name so secrets do not pass beyond the tool border. The connection will be retrieved again in the agent
  config = MIRSkillConfiguration(name=name, description=description, mir_connection=mir_connection.__connection_name, input_config=input_json, output_path=output_path, return_direct=return_direct)
  return config