import os
import subprocess


def run_echo(*args):
    print(*args)


def _find_executable_path(potential_executable):
    path = os.environ.get("PATH", "")
    directories = path.split(os.pathsep)
    for directory in directories:
        path_built = f"{directory}/{potential_executable}"
        if os.path.exists(path_built) and os.access(path_built, os.X_OK):
            return path_built


def run_unknown_command(unknown_command, *args):
    executable_path = _find_executable_path(unknown_command)

    if executable_path:
        subprocess.run([unknown_command, *args], check=False)
        return True
    else:
        return False


def run_type(*args):
    KNOWN_TYPES = {"echo": "builtin", "exit": "builtin", "type": "builtin"}

    potential_executable = " ".join(args)
    if potential_executable in KNOWN_TYPES:
        print(f"{potential_executable} is a shell builtin")
    else:
        executable_path = _find_executable_path(potential_executable)
        if not executable_path:
            print(f"{potential_executable}: not found")
        else:
            print(f"{potential_executable} is {executable_path}")
