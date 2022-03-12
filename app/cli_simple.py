import os

import click

from app.main_simple import print_welcome_message, print_incoming_message


@click.group()
@click.option("--config", default=None, help="Config file")
def cli(config):
    click.echo(config)
    os.environ["APP_CONFIG_FILE"] = config
        

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
