import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __add__(self, other):
        """
        Сложение классов с проверкой (self.quantity)
        """
        if not isinstance(other, Item):
            raise ValueError("Можно сложить только `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.")
        return self.quantity + other.quantity
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        full_price = self.price * self.quantity
        return full_price
    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        """
        Функция проверяет длину наименования товара, чтобы было не более 10 символов
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name
    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        """
        Создает экземпляры класса Item из данных в файле items.csv
        """
        cls.all.clear()
        try:
            with open(path, 'r', encoding='windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
                for row in rows:
                    Item(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))
        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
    @staticmethod
    def string_to_number(str_number):
        """
        Возвращает число из числа-строки
        """
        number = float(str_number)
        return int(number)