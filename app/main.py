import sys


def main():
    while True:
        command_run = read_command()
        if command_run == "exit":
            break


def read_command():
    sys.stdout.write("$ ")
    user_input = input()
    sys.stdout.write(f"{user_input}: command not found\n")

    return user_input.strip()


if __name__ == "__main__":
    main()
