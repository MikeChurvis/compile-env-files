import json
import os

log = '[CONFIG][LOADER] {}'.format


def load(path_to_config: str) -> dict:
  if not os.path.exists(path_to_config):
    raise FileNotFoundError(log(
      f"Cannot find a config file at ({path_to_config})."
      " Use command flag '-f <filepath>' to specify a different path."
    ))

  with open(path_to_config, 'r') as config_file:
    data = json.load(config_file)

  return data