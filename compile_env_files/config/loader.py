import json


def load_config_data(path_to_config: str) -> dict:
  with open(path_to_config, 'r') as config_file:
    data = json.load(config_file)

  return data