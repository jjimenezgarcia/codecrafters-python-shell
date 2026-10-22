import sys
from enum import StrEnum


class KnownMethods(StrEnum):
    EXIT = "exit"


def main():
    while True:
        command_run = read_command()
        if command_run == KnownMethods.EXIT:
            break


def read_command():
    sys.stdout.write("$ ")
    user_input = input().strip()

    if user_input not in KnownMethods:
        sys.stdout.write(f"{user_input}: command not found\n")

    return user_input


if __name__ == "__main__":
    main()
