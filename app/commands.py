import os


def run_echo(*args):
    print(*args)


def run_type(*args):
    KNOWN_TYPES = {"echo": "builtin", "exit": "builtin", "type": "builtin"}

    potential_executable = " ".join(args)
    if potential_executable in KNOWN_TYPES:
        print(f"{potential_executable} is a shell builtin")
    else:
        path = os.environ.get("PATH", "")
        directories = path.split(os.pathsep)
        for directory in directories:
            path_built = f"{directory}/{potential_executable}"
            if os.path.exists(path_built) and os.access(path_built, os.X_OK):
                print(f"{potential_executable} is {path_built}")
                return
        print(f"{potential_executable}: not found")
