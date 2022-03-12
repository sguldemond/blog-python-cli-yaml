import os

import click


@click.group()
@click.option("--config", default=None, help="Config file")
def cli(config):
    os.environ["APP_CONFIG_FILE"] = config
        

@click.command()
def welcome():
    from app.main import print_welcome_message
    print_welcome_message()


@click.command()
@click.argument('msg', required=True)
def echo(msg: str):
    from app.main import print_incoming_message
    print_incoming_message(msg)


cli.add_command(echo)
cli.add_command(welcome)


if __name__ == "__main__":
    cli()
