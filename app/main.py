import sys


def main():
    sys.stdout.write("$ ")
    read_command()


def read_command():
    user_input = input()

    sys.stdout.write(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
