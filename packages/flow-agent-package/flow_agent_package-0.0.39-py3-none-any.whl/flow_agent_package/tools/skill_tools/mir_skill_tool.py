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
def mir_skill(name: str, description: str, endpoint_name: str, input_config: str, output_path: str, deployment_name: str = None, return_direct: bool = True):
  """Creates a MIRSkillConfiguration for use in a Flow Agent"""

  # Validate the connection here to fail fast 
  input_json = json.loads(input_config)
  for key, value in input_json.items():
    if not isinstance(value, dict):
      raise Exception(input_structure_error)
    if value.get("type") == None:
      raise Exception(input_structure_error)
  print(f"Endpoint Name: {endpoint_name}")

  # Pass only connection name so secrets do not pass beyond the tool border. The connection will be retrieved again in the agent
  config = MIRSkillConfiguration(name=name, description=description, endpoint_name=endpoint_name, deployment_name=deployment_name, input_config=input_json, output_path=output_path, return_direct=return_direct)
  return config