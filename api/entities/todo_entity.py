"""Todo entity module."""


class Todo:
    """Todo entity."""

    def __init__(self, title, description, expiration_date, project) -> None:
        self.__title = title
        self.__description = description
        self.__expiration_date = expiration_date
        self.__project = project

    @property
    def title(self):
        """Title getter."""
        return self.__title

    @title.setter
    def title(self, title):
        """Title setter."""
        self.__title = title

    @property
    def description(self):
        """Description getter."""
        return self.__description

    @description.setter
    def description(self, description):
        """Description setter."""
        self.__description = description

    @property
    def expiration_date(self):
        """Expiration_date getter."""
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Expiration_date setter."""
        self.__expiration_date = expiration_date

    @property
    def project(self):
        """Project getter."""
        return self.__project

    @project.setter
    def project(self, project):
        """Project setter."""
        self.__project = project
