import click
import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent / 'vm.py'
sys.path.append(str(module_path.parent))


from vm import start, stop, connect
# breakpoint()


@click.group()
def cli():
    pass

cli.add_command(start, name="start")
cli.add_command(stop, name="stop")
cli.add_command(connect, name="connect")

if __name__ == '__main__':
    cli()
