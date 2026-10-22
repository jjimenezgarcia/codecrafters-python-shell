import os
import subprocess


def find_executable_path(potential_executable):
    path = os.environ.get("PATH", "")
    directories = path.split(os.pathsep)
    for directory in directories:
        path_built = f"{directory}/{potential_executable}"
        if os.path.exists(path_built) and os.access(path_built, os.X_OK):
            return path_built


def run_unknown_command(unknown_command, *args):
    executable_path = find_executable_path(unknown_command)

    if executable_path:
        subprocess.run([unknown_command, *args], check=False)
        return True
    else:
        return False
