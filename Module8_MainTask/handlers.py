from functools import wraps
from bot_assistant import AddressBook
from bot_assistant import Record


def input_error(func):
    """
    Декоратор для обробки помилок вводу.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "@input_error : KeyError : Contact not found."
        except ValueError:
            return "@input_error : ValueError : Give me name and phone please."
        except IndexError:
            return "@input_error : Index Error"
        except TypeError:
            return "@input_error : TypeError"
    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book : AddressBook) -> str:
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    return '\n'.join(ph.value for ph in record.phones)


@input_error
def show_all(book: AddressBook) -> str:
    return book


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Такого контакту не існує."
    record.birthday = birthday
    return "Дата дня народження успішно додана до контакту!"
    

@input_error
def show_birthday(args, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        return 'Такого контакту не існує.'
    return record.birthday.value.date()


@input_error
def birthdays(book: AddressBook) -> list:
    return book.get_upcoming_birthdays()


def exit_bot() -> str:
    return "Good bye!"

