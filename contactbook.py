import csv
import re
from datetime import date
from custom_errors import WrongInputError

class Contact:
    def __init__(self, name, last_name, address, phone, email, date_of_birth):
        self.name = name   # Ew. ograniczenie ilości znaków
        self.last_name = last_name  # Ew. ograniczenie ilości znaków
        self.address = address  # Ew. ograniczenie ilości znaków
        self.phone = phone  # Sprawdzanie poprawności wprowadzonego numeru telefonu
        self.email = email  # Sprawdzanie poprawności wprowadzonego email
        self.date_of_birth = date_of_birth  # Sprawdzanie poprawności formatu wprowadzonej daty urodzin
        self.contact = {
            "name": self.name,
            "last name": self.last_name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "date_of_birth": self.date_of_birth
            }

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone:str)->None:
        pattern=re.compile("\d{9}")
        if not pattern.fullmatch(new_phone):
            raise WrongInputError(f"Incorrect phone number: {new_phone}")
        else:
            self._phone=new_phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email:str)->None:   
        pattern=re.compile("[a-zA-Z][\w.-]+@\w+\.\w{2,}")
        if not pattern.fullmatch(new_email):
            raise WrongInputError(f"Incorrect email: {new_email}")
        else:
            self._email=new_email

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth:str)->None: #date expected to be in dd.mm.yyyy format
        pattern=re.compile("\d{2}\.\d{2}\.\d{4}")
        if not pattern.fullmatch(new_date_of_birth):
            raise WrongInputError(f"Incorrect date format: {new_date_of_birth}")
        ymd_int_date_of_birth=[int(str_number) for str_number in new_date_of_birth.split('.')][::-1]
        try:
            self._date_of_birth=date(*ymd_int_date_of_birth)
        except ValueError as e:
            if str(e) == 'month must be in 1..12':
                raise WrongInputError('Incorrect month number')
            elif str(e) =='day is out of range for month':
                raise WrongInputError('Wrong day number for this month')
            else:
                raise ValueError(e)



class ContactBook:
    def add_contact(self):
        with open("contact_book.csv", "a", newline="") as fh:
            field_names = ["name", "last name", "address", "phone", "email", "date_of_birth"]
            writer = csv.DictWriter(fh, fieldnames=field_names)
            writer.writeheader()
            writer.writerow() #Instancja klasy Contact w formie słownika

    def edit_contact(self):
        pass

    def remove_contact(self):
        pass

    def search(self):
        pass

    def show_all_contacts(self):
        pass

    def birthday_of_contact(self, days_to_birthday):
        pass