import requests
import os
from classes.abstract_classes import AbstractApi


class SuperJobAPI(AbstractApi):
    """
    Класс для работы с API платформы SuperJob
    """

    def __init__(self) -> None:
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.secret_key = os.getenv("SUPER_JOB_KEY")

    def get_vacancies(self, text: str) -> list[dict]:
        """
        Получает вакансии через API SuperJob
        """
        try:
            vacancies = requests.get(
                self.url, headers={"X-Api-App-Id": self.secret_key}, params={"keywords": {text}, "no_agreement": 1}
            )
            return vacancies.json()["objects"]
        except Exception as error:
            raise Exception(f"Ошибка {error}")
