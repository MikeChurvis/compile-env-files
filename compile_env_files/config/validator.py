import re
from utils import islist

log = "[CONFIG][VALIDATION] {}".format


def validate_config_data(config_data: dict) -> None:
  """
  Raises an error if any aspect of the configuration data is invalid.
  """

  validate_consumers_attribute(config_data)
  validate_variables_attribute(config_data)
  validate_all_variables_use_declared_consumers(config_data)
  # TODO: detect consumer-key pair duplicates and raise KeyError


def validate_all_variables_use_declared_consumers(config_data: dict) -> None:
  """
  Raises an error if any element in the top-level attribute 'variables' 
  defines an environment variable key for a consumer that is not declared 
  in the top-level attribute 'consumers'.
  """
  declared_consumers = { consumer for consumer in config_data['consumers'].keys() }

  for label, data in config_data['variables'].items():
    for consumer in data['consumers'].keys():
      if consumer not in declared_consumers:
        raise KeyError(log(
          f"variables['{label}'] uses an undeclared consumer '{consumer}'."
          " Add this consumer to the top-level 'consumers' attribute to use it."
        ))


def validate_variable_definition(label: str, data: dict) -> None: 
  """
  Raises an error if any of the properties of a variable definition are invalid.
  """
  
  if not isinstance(data, dict):
    raise TypeError(log(
      f"variables['{label}'] must be an object."
    ))

  if 'value' not in data:
    raise AttributeError(log(
      f"variables['{label}'] is missing a 'value' attribute."
    ))

  if 'consumers' not in data:
    raise AttributeError(log(
      f"variables['{label}'] is missing a 'consumers' attribute."
    ))

  value = data['value']
  consumers = data['consumers']

  if not isinstance(value, (str, int, float, bool)):
    raise TypeError(log(
      f"variables['{label}'].value must be a string, number, or boolean."
    ))

  if not isinstance(consumers, dict):
    raise TypeError(log(
      f"variables['{label}'].consumers must be an object."
    ))

  if len(consumers) == 0:
    raise ValueError(log(
      f"variables['{label}'].consumers must contain at least one element."
    ))

  for consumer, export_key in consumers.items():
    if not (isinstance(export_key, str) or islist(export_key, str)):
      raise TypeError(log(
        f"variables['{label}'].consumers['{consumer}']"
        " must be either a string or a list of strings."
      ))

    if isinstance(export_key, list):
      keys = export_key
    else:
      keys = [export_key]

    for key in keys:
      if not re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", key):
        raise ValueError(log(
          f"variables['{label}'].consumers['{consumer}']: '{key}'"
          " is not a valid environment variable key"
          " (must match regex [a-zA-Z_][a-zA-Z0-9_]*)"
        ))


def validate_variables_attribute(config_data: dict) -> None:
  """
  Raises an error if the config's top-level 'variables' attribute 
  is missing or has an invalid shape.
  """

  if 'variables' not in config_data: 
    raise AttributeError(log(
      "Missing top-level attribute: 'variables'."
    ))

  variables = config_data['variables']

  if not isinstance(variables, dict):
    raise TypeError(log(
      "Attribute 'variables' must be an object (\"variables\": {...})."
    ))
  
  if len(variables) == 0:
    raise ValueError(log(
      "Attribute 'variables' must contain at least one element."
    ))

  for label, data in variables.items():
    validate_variable_definition(label, data)


def validate_consumers_attribute(config_data: dict) -> None:
  """
  Raises an error if the config's top-level 'consumers' attribute 
  is missing or has an invalid shape.
  """

  if 'consumers' not in config_data:
    raise AttributeError(log(
      "Missing top-level attribute: 'consumers'."
    ))
  
  consumers = config_data['consumers']

  if not isinstance(consumers, dict):
    raise TypeError(log(
      "Attribute 'consumers' must be an object (\"consumers\": {...})."
    ))
  
  if len(consumers) == 0:
    raise ValueError(log(
      "Attribute 'consumers' must contain at least one element."
    ))

  for consumer, output_paths in consumers.items():
    if not (isinstance(output_paths, str) or islist(output_paths, str)):
      raise TypeError(log(
        f"consumers['{consumer}'] must be a filepath or list of filepaths."
      ))




  