def run_echo(*args):
    print(*args)


def run_type(*args):
    KNOWN_TYPES = {"echo": "builtin", "exit": "builtin", "type": "builtin"}

    args_as_string = " ".join(args)
    if args_as_string in KNOWN_TYPES:
        print(f"{args_as_string} is a shell builtin")
    else:
        print(f"{args_as_string}: not found")
