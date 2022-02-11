import sys
import os
from config import load_config_data, validate_config_data, blank
from env_files import generate_env_data, write_env_files


def compile_env_files():
  config_filename = '.env.config.json'

  if '-f' in sys.argv:
    flag_index = sys.argv.index('-f')
    try:
      config_filename = sys.argv[flag_index + 1]
    except IndexError:
      raise ValueError("Command argument value missing (-f <filename>).")

  config_filepath = os.path.join(os.getcwd(), os.path.normpath(config_filename))

  config = load_config_data(config_filepath)
  validate_config_data(config)

  env_data = generate_env_data(config)
  write_env_files(env_data)

def generate_blank_config():
  with open('.env.config.json', mode='w') as config_file:
    config_file.write(blank.config)