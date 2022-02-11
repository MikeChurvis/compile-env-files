import sys
import os
from .config import load_config_data, validate_config_data, blank
from .env_files import generate_env_data, write_env_files

log = '[CONFIG][COMMAND] {}'.format


def compile_env_files():
  config_filepath = '.env.config.json'

  if '-f' in sys.argv:
    flag_index = sys.argv.index('-f')
    try:
      config_filepath = sys.argv[flag_index + 1]
    except IndexError:
      raise ValueError(log(
        "Command flag is missing a value (-f <filepath>)."
      ))

  if not os.path.isabs(config_filepath):
    config_filepath = os.path.join(os.getcwd(), os.path.normpath(config_filepath))

  config = load_config_data(config_filepath)
  validate_config_data(config)

  env_data = generate_env_data(config)
  write_env_files(env_data)


def generate_blank_config():
  with open('.env.config.json', mode='w') as config_file:
    config_file.write(blank.config)