from src.item import Item


class MixinLang:
    """
    Класс-миксин, который хранит и изменяет раскладку клавиатуры
    """
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Метод для изменения языка (раскладки клавиатуры)
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):
    """
    Класс, который наследуется от класса Item и имеет дополнительный атрибут и метод
    по изменению раскладки клавиатуры из класса-миксина
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)

