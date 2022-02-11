
def generate_data(config_data):
  consumers_variables = { consumer: [] for consumer in config_data['consumers'] }

  for label, var_data in config_data['variables'].items():
    value = var_data['value']

    for consumer, keys in var_data['consumers'].items():
      if not isinstance(keys, list):
        keys = [keys]

      for key in keys:
        consumers_variables[consumer].append(f'{key}="{value}"')

  env_file_contents = {}

  for consumer, output_files in config_data['consumers'].items():
    if not isinstance(output_files, list):
      output_files = [output_files]

    for filepath in output_files:
      env_file_contents[filepath] = consumers_variables[consumer]

  return env_file_contents

  

