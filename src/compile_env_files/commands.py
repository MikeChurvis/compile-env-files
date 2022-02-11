import sys
import os
from compile_env_files import config, env_files

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

  config_data = config.load(config_filepath)
  config.validate(config_data)

  env_data = env_files.generate_data(config_data)
  env_files.write(env_data)


def generate_blank_config():
  with open('.env.config.json', mode='w') as config_file:
    config_file.write(config.blank_template)