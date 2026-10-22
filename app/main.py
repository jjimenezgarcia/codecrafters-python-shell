import sys
from collections.abc import Callable
from enum import StrEnum

from app.commands import run_echo


class KnownCommands(StrEnum):
    handler: Callable[..., None] | None

    EXIT = "exit"
    ECHO = ("echo", run_echo)

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
        command_run = read_command()
        if command_run == KnownCommands.EXIT:
            break


def read_command():
    sys.stdout.write("$ ")
    user_input = input().strip().split()
    command, *args = user_input

    if command not in KnownCommands:
        sys.stdout.write(f"{user_input}: command not found\n")

    executable_command = KnownCommands(command)
    executable_command.execute(*args)
    return user_input


if __name__ == "__main__":
    main()
