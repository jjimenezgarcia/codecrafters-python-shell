import sys
from collections.abc import Callable
from enum import StrEnum

from app.commands import run_echo, run_type, run_unknown_command

STATUS = {"exit": False}


class KnownCommands(StrEnum):
    handler: Callable[..., None] | None

    EXIT = ("exit", lambda: STATUS.update(exit=True))
    ECHO = ("echo", run_echo)
    TYPE = ("type", run_type)

    def __new__(cls, command_name, handler=None):
        obj = str.__new__(cls, command_name)
        obj._value_ = command_name
        obj.handler = handler
        return obj

    def execute(self, *args, **kwargs):
        if self.handler is not None:
            self.handler(*args, **kwargs)


def main():
    while True:
        read_command()
        if STATUS["exit"]:
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
