import datetime
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s:%(asctime)s - %(message)s'
)


class Student:
    def __init__(self, name: str, surname: str, birthdate, height=160):

        if type(name) != str:
            raise TypeError(f"Name must be str type. Not a '{type(name)}'")

        if type(surname) != str:
            raise TypeError(f"Surname must be str type. Not a '{type(surname)}'")

        if type(birthdate) != str:
            raise TypeError(f"Birthdate must be str type. Not a '{type(birthdate)}'")

        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        if self.birthdate.date() > datetime.date.today():
            raise ValueError(f"Birthdate '{self.birthdate.date()}' is in the future.")

        if not isinstance(height, (int, float)):
            raise TypeError(f"Height must be int or float type. Not a '{type(height)}'")
        if height <= 0:
            raise ValueError("Height must be greater than 0.")

        self.name = name
        self.surname = surname
        self.height = height

        logging.info(f"Student created: {self.name} {self.surname}")
    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now() - self.birthdate).days // 365
        return age
try:
    first_student = Student("Bank", 'Natan', '24.01.2011', 165)
    second_student = Student('Oleg', 'Palkin', '25.05.2025', 220)
except (TypeError, ValueError) as error:
    logging.exception("Exception occurred: %s", error)
