if __name__ == "__main__":
    class Vehicle:
        def __init__(self, name: str, number_of_wheels: int, type_of_engine: str):
            """
             Базовый класс транспорта.
             
            :param name: наименование вида транспорта
            :param number_of_wheels: количество колес
            :param type_of_engine: тип двигателя
            
            Пример:
            >>> car_1 = Vehicle("Автомобиль", 4, "Внутреннего сгорания")
            """
            if not isinstance(name, str):
                raise TypeError("Наименование вида транспорта должно быть типа str")
            self._name = name  # после задания вида транпорта этот параметр уже нельзя изменить

            if not isinstance(type_of_engine, str):
                raise TypeError("Тип двигателя должен быть типа str")
            self.type_of_engine = type_of_engine

            if not isinstance(number_of_wheels, int):
                raise TypeError("Количество колес должно быть типа int")
            if number_of_wheels <= 0:
                raise ValueError("Количество колес должно быть положительным числом")
            self.number_of_wheels = number_of_wheels

        @property
        def name(self):
            return self._name

        def __str__(self):
            """
            Определяет поведение функции str()
            :return: выводит f-строку со значением каждого атрибута

            Пример:
            >>> car_1 = Vehicle("Автомобиль", 4, "Внутреннего сгорания")
            >>> print(car_1)
            >>> Вид транспорта: Автомобиль
            >>> Количество колес: 4
            >>> Тип двигателя: Внутреннего сгорания
            """
            return f"Вид транспорта: {self._name}\nКоличество колес: {self.number_of_wheels}\n" \
                   f"Тип двигателя: {self.type_of_engine}"

        def __repr__(self):
            """
            Определяет поведение функции repr()
            :return:возвращает строку, показывающую,как может быть инициализирован экземпляр

            Пример:
            >>> car_1 = Vehicle("Автомобиль", 4, "Внутреннего сгорания")
            >>> print(repr(car_1)
            >>> Vehicle(name='Автомобиль', number_of_wheels=4,type_of_engine='Внутреннего сгорания')
            """
            return f"{self.__class__.__name__}(name={self._name!r}, number_of_wheels={self.number_of_wheels!r}," \
                   f"type_of_engine={self.type_of_engine!r})"

        def close_the_door(self) -> None:
            """
            Метод, закрывающий дверь транспорта
            :return: None
            """
            ...

        def number_of_exhausts_at_the_moment(self, time) -> int | float:
            """
            Функция, вычисляющая количество выхлопов на данный момент.
            Рассчитывается по формуле с учетом текущего времени.
            :param time: время езды транспорта
            :return: количество выхлопов на текущий момент
            """
            if not isinstance(time, int | float):
                raise TypeError("Время должно быть типа int или float")
            if time < 0:
                raise ValueError("Время должно быть положительным")
            ...


    class ElectricCar(Vehicle):
        def __init__(self, name: str, number_of_wheels: int, type_of_engine: str, battery_capacity: float):
            """
            Дочерний класс транспорта - электромобиль.
            :param name: наименование вида транспорта
            :param number_of_wheels: количество колес
            :param type_of_engine: тип двигателя
            :param battery_capacity: емкость аккумулятора электромобиля

            Пример:
            >>> electric_car_1 = ElectricCar("Электромобиль", 4, "Аккумулятор", 40)
            """
            super().__init__(name, number_of_wheels, type_of_engine)
            if not isinstance(battery_capacity, int | float):
                raise TypeError("Емкость аккумулятора должна быть типа int или float")
            if battery_capacity <= 0:
                raise ValueError("Емкость аккумулятора должна быть положительным числом")
            self.battery_capacity = battery_capacity

        def __str__(self):
            return f"{super().__str__()}\nЕмкость батареи: {self.battery_capacity} кВт/ч"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, number_of_wheels={self.number_of_wheels!r}," \
                   f" type_of_engine={self.type_of_engine!r}, battery_capacity={self.battery_capacity!r})"

        def number_of_exhausts_at_the_moment(self, time) -> None:
            """
            Функция, вычисляющая количество выхлопов на данный момент.
            В электромобиле нет вредных выхлопов, поэтому возвращаем None.
            :param time: время езды электромобиля
            :return: None
            """
            return None
    pass

