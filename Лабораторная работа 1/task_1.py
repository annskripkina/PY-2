import doctest


class TV:
    def __init__(self, total_amount_of_channels: int, tv_on=False):
        """
        Создание и подготовка к работе объекта "Телевизор"

        :param total_amount_of_channels: Количество каналов, доступных на данном телевизоре
        :param tv_on: Состояние телевизора (Включен/ Выключен). По умолчанию выключен

        Пример:
        >>> tv = TV(20, True) # Телевизор включен
        >>> tv = TV(10) # Телевизор выключен
        """
        if not isinstance(total_amount_of_channels, int):
            raise TypeError("Общее количество каналов должно быть типа int")
        if total_amount_of_channels <= 0:
            raise ValueError("Общее количество каналов должно быть положительным числом")
        self.total_amount_of_channels = total_amount_of_channels

        if not isinstance(tv_on, bool):
            raise TypeError("Показатель состояния телевизора должен быть типа bool")
        self.tv_on = tv_on

    def status_of_tv(self, status: bool) -> None:
        """
        Функция, которая изменяет состояние телевизора: включен/выключен: True - ТВ включен, False - ТВ выключен

        :param  status: Желаемое состояние телевизора

        :raise TypeError: Функция, которая задает состояние телевизора, должна быть типа bool

        :return: Новое состояние телевизора

        Пример:
        >>> tv = TV(30, True)
        >>> tv.status_of_tv(False) # Выключаем ТВ
        """
        if not isinstance(status, bool):
            raise TypeError("Функция, которая задает состояние телевизора, должна быть типа bool")
        ...

    def set_channel(self, channel: int) -> None:
        """
        Функция, которая включает желаемый канал

        :param channel: Номер канала

        :raise ValueError: Значение канала превышает количество каналов
        :raise TypeError: Функция задания канала вызывается при выключенном телевизоре

        :return: Новое значение канала

        Пример:
        >>> tv = TV(30, True)
        >>> tv.set_channel(5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


class Mouse:
    def __init__(self, dpi: int, number_of_buttons: int, backlight=False):
        """
        Создание и подготовка к работе объекта "Компьютерная мышка"

        :param dpi: Разрешение датчика, лежит в пределах 200-12000 dpi
        :param number_of_buttons: Количество функциональных кнопок. Изначально количество - 6, добавить можно еще 4
        :param backlight: Наличие подсветки

        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        """
        if not isinstance(dpi, int):
            raise TypeError("Разрешение датчика должно быть типа int")
        if (dpi < 200) or (dpi > 12000):
            raise ValueError("Разрешение датчика лежит в пределах 200-12000 dpi")
        self.dpi = dpi

        if not isinstance(number_of_buttons, int):
            raise TypeError("Количество функциональных кнопок мышки должно быть типа int")
        if (number_of_buttons < 6) or (number_of_buttons > 10):
            raise ValueError("Количество функциональных кнопок мышки не может быть меньше 6 или больше 10")
        self.number_of_buttons = number_of_buttons

        if not isinstance(backlight, bool):
            raise TypeError("Показатель наличия подсветки должен быть типа bool")
        self.backlight = backlight

    def backlight_check(self) -> None:
        """
        Функция, которая проверяет наличие подсветки у мышки
            
        :return: Светится ли мышка
            
        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        >>> mouse1.backlight_check()
        """
        ...

    def add_buttons(self, added_buttons: int) -> int:
        """
        Функция добавления функциональных кнопок мышки

        :param added_buttons: Число добавленных кнопок

        :raise ValueError: Если количество изначально заданных кнопок вместе с количеством добавленных превышает 10, вызывается эта ошибка
        :raise TypeError: Число добавленных кнопок должно быть типа int

        :return: Новое значение функциональных кнопок

        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        >>> mouse1.added_buttons(3) # На выходе получится 9
        """
        if not isinstance(added_buttons, int):
            raise TypeError("Число добавленных кнопок должно быть типа int")
        ...


class XmasTree:
    def __init__(self, height: int, xmas_decorations):
        """
        Создание и подготовка к работе объекта "Новогодняя елка"

        :param height: Высота елки в см
        :param amount_of_decorations: Количество елочных игрушек, либо их отсутствие

        Пример:
         >>> xmas_tree = XmasTree(180, False) # Высотка елки 180 см, не украшена
        """
        if not isinstance(height, int):
            raise TypeError(" Высотка елки должна быть типа int")
        if height <= 0:
            raise ValueError("Высотка елки должна быть положительным числом")
        self.height = height

        if not isinstance(xmas_decorations, int | None):
            raise TypeError("Количество новогодних украшений должно быть типа int, в случае их отсутствия - None")
        self.xmas_decorations = xmas_decorations

    def opportunity_of_decoration_with_star(self, height_of_person: int) -> bool:
        """
        Функция, которая проверяет, может ли человек установить звезду на вершину елки

        :param height_of_person: Рост человека

        :raise TypeError: Рост человека должен быть типа int

        :return: Сможет ли человек установить звезду

        Пример:
         >>> xmas_tree = XmasTree(180, False)
         >>>xmas_tree.opportunity_of_decoration_with_star(150) # True, При сравнении будет учитываться еще высота руки, примерно равная 40 см
        """
        if not isinstance(height_of_person, int):
            raise TypeError("Рост человека должен быть типа int")
        ...

    def is_the_tree_decorated(self) -> bool:
        """
        Функция, которая определяет, украшена ли елка

        :return: Украшена ли елка

        Пример:
        >>> xmas_tree = XmasTree(180, 20)
         >>>xmas_tree.is_the_tree_decorated() # True, елка украшена
        """
        ...
