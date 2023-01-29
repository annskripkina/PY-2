class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name

        @property
        def name(self):
            return self._name

        self._author = author

        @property
        def author(self):
            return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        if not isinstance(self.pages, int):
            raise TypeError("Количество страниц должно быть целочисленным типом")
        if self.pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")

    def __str__(self):
        return f"{super().__str__()}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        if not isinstance(self.duration, int | float):
            raise TypeError("Продолжительность книги должна быть выражена в виде числа")
        if self.duration < 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")

    def __str__(self):
        return f"{super().__str__()}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.duration!r})"

