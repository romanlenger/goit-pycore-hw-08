import pickle
from bot_assistant.book import AddressBook


def save_data(book, filename: str):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename: str):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
