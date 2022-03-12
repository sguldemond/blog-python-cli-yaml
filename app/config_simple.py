import os

import yaml


config_file = os.getenv("APP_CONFIG_FILE")
print(f"Config file set to: ", config_file)

with open(config_file, 'r') as file:
    config = yaml.safe_load(file)


WELCOME_MSG = config.get('welcome_msg', None)


if __name__ == "__main__":
    print(WELCOME_MSG)