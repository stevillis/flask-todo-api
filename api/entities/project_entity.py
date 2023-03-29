"""Project entity module."""


class Project:
    """Project entity."""

    def __init__(self, name, description) -> None:
        self.__name = name
        self.__description = description

    @property
    def name(self):
        """name getter."""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter."""
        self.__name = name

    @property
    def description(self):
        """Description getter."""
        return self.__description

    @description.setter
    def description(self, description):
        """Description setter."""
        self.__description = description
