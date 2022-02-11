import os

def write_env_files(env_data):
  for filepath, data in env_data.items():
    target_directory = os.path.dirname(filepath)
    if not os.path.exists(target_directory):
      os.makedirs(target_directory)

    with open(filepath, mode='w') as env_file:
      env_file.write('\n'.join(data))