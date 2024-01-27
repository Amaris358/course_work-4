import json
import os
from pathlib import Path
from classes.abstract_classes import Saver

FILE_NAME = Path(__file__).parent.parent.joinpath("data", "vacancies.json")


class SaverJSON(Saver):
    """
    Класс для работы с файлом формата json, в котором хранятся данные о вакансиях
    """

    def add_vacancies(self, vacancies):
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(vacancies, file, indent=4, ensure_ascii=False)
        except Exception as error:
            raise Exception(f'Ошибка {error}')

    def get_by_salary(self, salary_min, salary_max):
        """
        """
        try:
            with open(FILE_NAME, encoding="utf-8") as file:
                data = json.load(file)
            return [
                vacancy
                for vacancy in data
                if vacancy["Зарплата минимальная"] and vacancy["Зарплата максимальная"] and vacancy["Зарплата минимальная"] >= salary_min and vacancy["Зарплата максимальная"] <= salary_max
            ]
        except Exception as error:
            raise Exception(f"Ошибка {error}")

    def delete_vacancies(self) -> None:
        """
        Удаляет файл с вакансиями
        """
        try:
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
        except Exception as error:
            raise Exception(f"Ошибка {error}")


