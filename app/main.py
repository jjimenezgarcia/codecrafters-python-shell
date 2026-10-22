import sys

from app.commands import KnownCommands
from app.helpers import run_unknown_command
from app.state import state


def main():
    while True:
        read_command()
        if state.exit:
            break


def read_command():
    sys.stdout.write("$ ")
    user_input = input().strip().split()
    command, *args = user_input

    try:
        executable_command = KnownCommands(command)
        executable_command.execute(*args)
    except ValueError:
        if not run_unknown_command(command, *args):
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
