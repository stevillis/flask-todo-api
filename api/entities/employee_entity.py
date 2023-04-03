"""Employee entity module."""


class Employee:
    """Employee entity."""

    def __init__(self, name, birth_date) -> None:
        self.__name = name
        self.__birth_date = birth_date

    @property
    def name(self):
        """Name getter."""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter."""
        self.__name = name

    @property
    def birth_date(self):
        """Birthdate getter."""
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Birthdate setter."""
        self.__birth_date = birth_date
