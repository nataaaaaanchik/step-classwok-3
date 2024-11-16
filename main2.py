import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s:%(asctime)s - %(message)s'
)


class Animal:
    def __init__(self, name: str, species: str, birthdate: str, weight: float):
        try:
            if not isinstance(name, str):
                raise TypeError(f"Имя должно быть строкой. Передан тип: {type(name)}")
            if not isinstance(species, str):
                raise TypeError(f"Вид животного должен быть строкой. Передан тип: {type(species)}")
            if not isinstance(birthdate, str):
                raise TypeError(f"Дата рождения должна быть строкой. Передан тип: {type(birthdate)}")

            self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
            if self.birthdate.date() > datetime.date.today():
                raise ValueError(f"Дата рождения {self.birthdate.date()} не может быть в будущем.")

            if not isinstance(weight, (int, float)):
                raise TypeError(f"Вес должен быть числом. Передан тип: {type(weight)}")
            if weight <= 0:
                raise ValueError("Вес должен быть больше нуля.")

            self.name = name
            self.species = species
            self.weight = weight

            logging.debug(f"Объект Animal создан: Имя={self.name}, Вид={self.species}")
        except Exception as error:
            logging.error(f"Ошибка при создании объекта Animal: {error}")
            raise

    def display_info(self):
        try:
            info = (f"Имя: {self.name}\n"
                    f"Вид: {self.species}\n"
                    f"Дата рождения: {self.birthdate.strftime('%d.%m.%Y')}\n"
                    f"Вес: {self.weight} кг")

            print(info)

            logging.debug(f"Информация об объекте Animal: {self.name}\n{info}")
        except Exception as error:
            logging.error(f"Ошибка при выводе информации: {error}")
            raise


try:

    first_animal = Animal("Шарик", "Собака", "12.05.2015", 15.5)
    second_animal = Animal("Мурзик", "Кот", "30.12.2030", 4.0)
except Exception as e:
    logging.error(f"Исключение: {e}")

try:
    first_animal.display_info()
except Exception as e:
    logging.error(f"Исключение при вызове display_info: {e}")
