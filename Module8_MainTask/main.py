from typing import Tuple, List
from handlers import *
from funcs.data import load_data, save_data


DATA = r'Module8_MainTask\bot_assistant\book.pickle'

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    input_parts = user_input.strip().split()
    command = input_parts[0].lower()
    args = input_parts[1:]
    return command, args


def main():
    book = load_data(DATA)

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book, DATA)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
    