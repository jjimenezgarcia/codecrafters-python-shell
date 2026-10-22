import os
from collections.abc import Callable
from enum import StrEnum

from app.helpers import find_executable_path
from app.state import state


## --- KNOWN COMMANDS ----
def run_echo(*args):
    print(*args)


def run_type(*args):
    potential_executable = " ".join(args)
    if potential_executable in KnownCommands:
        print(f"{potential_executable} is a shell builtin")
    else:
        executable_path = find_executable_path(potential_executable)
        if not executable_path:
            print(f"{potential_executable}: not found")
        else:
            print(f"{potential_executable} is {executable_path}")


def run_cd(*args):
    potential_path = "".join(*args)
    full_route = os.path.expanduser(potential_path)
    try:
        os.chdir(full_route)
    except FileNotFoundError:
        print(f"cd: {full_route}: No such file or directory")
    except NotADirectoryError:
        print(f"cd: {full_route}: Not a directory")
    except PermissionError:
        print(f"cd: {full_route}: Permission denied")


class KnownCommands(StrEnum):
    handler: Callable[..., None] | None

    EXIT = ("exit", lambda: state.set_exit(True))
    ECHO = ("echo", run_echo)
    TYPE = ("type", run_type)
    PWD = ("pwd", lambda: print(os.getcwd()))
    CD = ("cd", run_cd)

    def __new__(cls, command_name, handler=None):
        obj = str.__new__(cls, command_name)
        obj._value_ = command_name
        obj.handler = handler
        return obj

    def execute(self, *args, **kwargs):
        if self.handler is not None:
            self.handler(*args, **kwargs)
