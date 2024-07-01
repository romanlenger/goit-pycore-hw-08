from .record import Record
from datetime import date
from collections import UserDict
from typing import List, Dict

from funcs.upcoming_bitrhdays import adjust_for_weekend, date_to_string

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            return "record not found."
        
    def get_upcoming_birthdays(self) -> List[Dict]:
        upcoming_birthdays = []
        today = date.today()
        for rec in self.data.values():
            birthday_this_year = rec.birthday.value.replace(year=today.year).date()

            # Перевірка, чи не буде припадати день народження вже наступного року
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Перенесення дати привітання на наступний робочий день, якщо день народження припадає на вихідний
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            
            # Перевірка, чи день народження випадає протягом наступних 7 днів
            if 0 <= (birthday_this_year - today).days <= 7:
                congratulation_date_str = date_to_string(birthday_this_year)
                upcoming_birthdays.append({"Name": rec.name.value, "Congratulation_Date": congratulation_date_str})

        return upcoming_birthdays
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    


