from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """
    Абстарктный класс для работы с платформами через API
    """
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """
        """
        pass


class Saver(ABC):
    """
    Абстрактный класс для работы с файлом JSON
    """

    @abstractmethod
    def add_vacancies(self, *args, **kwargs):
        """
        Метод для добавления вакансии в файл
        """
        pass

    @abstractmethod
    def get_by_salary(self, *args, **kwargs):
        """
        Метод для сортировки вакансии по 
        """
        pass

    @abstractmethod
    def delete_vacancies(self, *args, **kwargs):
        """
        Удаляет все вакансии
        """
        pass



