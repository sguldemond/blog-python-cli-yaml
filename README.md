# Building a CLI application in Python (& some YAML)

Around four years ago I started programming in Python and ever since I really enjoy it. At the same time I started using more Linux, first for deploying small experimental applications and later as my personal OS. I really like to find my way around Linux using the terminal, and the concept of a command line interface spoke to me.

When there is a good enough reason, for a project, I like to create small applications in Python with a CLI. I would like to share how I've made my most recent CLI with a YAML config file.

## Setup

Firsly I'll setup a small application to create an CLI for:
```
➜  python-cli-yaml
.
├── app
│   ├── main.py
│   ├── cli.py
│   ├── config.py
│   └── __init__.py
└── venv
```

The next thing to do is to make sure the `PYTHONPATH` environment variable is set. I make sure I'm inside the root folder of the project (`python-cli-yaml`) and then do `export PYTHONPATH=$(pwd)`.

## Code
### Create simple functions

In need some functions that I will call later, `main.py`:
```python
WELCOME_MSG = "Hello world!"

def print_welcome_message():
    print(WELCOME_MSG)


def print_incoming_message(msg: str):
    print("Incoming message:", msg)


if __name__ == "__main__":
    print_welcome_message()
    print_incoming_message("Foobar!")
```
We can test these functions simply by running the file `python app/main.py`


### Setup CLI

I'm using Click for this, so installed it: `pip install click`

In another file I can now start setting up my CLI code, `cli.py`:
```python
import click

from app.main import print_welcome_message, print_incoming_message


@click.group()
def cli():
    pass
        

@click.command()
def welcome():
    print_welcome_message()


@click.command()
@click.argument('msg', required=True)
def echo(msg: str):
    print_incoming_message(msg)


cli.add_command(welcome)
cli.add_command(echo)


if __name__ == "__main__":
    cli()
```
With this code both simple functions from main can be called:
```bash
python app/cli.py welcome
python app/cli.py echo 'Hi there!'
```

### Setup YAML

To make it a little bit more interesting I add a configuration file to read, e.g. the welcome message from:
```bash
touch app-config.txt
echo 'welcome_msg: "Hey you!"' >> app-config.txt 
```

I need some more code to parse this file, `config.py`:
```python
import os

import yaml


config_file = os.getenv("APP_CONFIG_FILE")
print(f"Config file set to: ", config_file)

with open(config_file, 'r') as file:
    config = yaml.safe_load(file)

WELCOME_MSG = config.get('welcome_msg', None)


if __name__ == "__main__":
    print(WELCOME_MSG)
```
I'm using a environment variable to point to the config file. Later on I will set this variable from the CLI code. To test this I can run:
```bash
export APP_CONFIG_FILE=app-config.yml
python config.py
```

Now I have all the elements ready, I just need to connect the CLI with the config code.
I add a argument to the main cli function and set the input as enviroment variable, `cli.py`:
```python
import os

@click.group()
@click.option("--config", default=None, help="Config file")
def cli(config):
    os.environ["APP_CONFIG_FILE"] = config

...
```

Now I can run the CLI file and point to the config file from there, no need to set `APP_CONFIG_FILE` manually:
```bash
python app/cli_simple.py --config=app-config.yml welcome
```

