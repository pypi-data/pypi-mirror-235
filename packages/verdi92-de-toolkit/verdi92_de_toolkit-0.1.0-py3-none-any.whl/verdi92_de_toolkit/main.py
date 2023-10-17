#click is a Python package and a CLI creation framework that simplifies the process of building command-line tools in Python.
import click
#  with .vm, Python looks for the vm module within the same package as your main.py script.
from .vm import start
from .vm import stop
from .vm import connect


@click.group()
def cli():
    pass

cli.add_command(start)
cli.add_command(stop)
cli.add_command(connect)

if __name__ == '__main__':
    cli()
