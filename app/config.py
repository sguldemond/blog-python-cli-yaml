import os
import sys

import yaml

project_root = os.getenv("PYTHONPATH")
if project_root is None:
    project_root = os.getcwd()

config_file = os.getenv("APP_CONFIG_FILE")
if config_file is None:
    config_file = f"{project_root}/app-config.yml"

if not os.path.exists(config_file):
    sys.exit("Config file path not found! Exiting...")

print(f"Config file set to: ", config_file)

with open(config_file, 'r') as file:
    config = yaml.safe_load(file)
    

WELCOME_MSG = config.get('welcome_msg', None)


if __name__ == "__main__":
    print(WELCOME_MSG)
