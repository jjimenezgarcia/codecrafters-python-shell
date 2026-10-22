import sys


def main():
    while True:
        read_command()


def read_command():
    sys.stdout.write("$ ")
    user_input = input()

    sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
