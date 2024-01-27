from datetime import datetime

from classes.vacancies_class import Vacancy


def get_hh_vacancies(vacancies: list[dict]) -> list[Vacancy]:
    """
    Инициализирует полученные вакансии HeadHunter в экземпляры Класса Vacancy
    """
    try:
        list_ = []
        if not vacancies:
            return []
        for vacancy in vacancies:
            list_.append(
                Vacancy(
                    vacancy_id=vacancy["id"],
                    vacancy_url=vacancy["alternate_url"],
                    publication_date=datetime.fromisoformat(vacancy["published_at"]).strftime("%d.%m.%Y"),
                    experience=vacancy["experience"]["name"],
                    vacancy_name=vacancy["name"],
                    salary_min=vacancy["salary"]["from"],
                    salary_max=vacancy["salary"]["to"]
                )
            )
        return list_
    except Exception as error:
        raise Exception(f"Ошибка {error}")


def get_sj_vacancies(vacancies: list[dict]) -> list[Vacancy]:
    """
    Инициализирует полученные вакансии SuperJob в экземпляры Класса Vacancy
    """
    try:
        list_ = []
        if not vacancies:
            return []
        for vacancy in vacancies:
            list_.append(
                Vacancy(
                    vacancy_id=vacancy["id"],
                    vacancy_url=vacancy["link"],
                    publication_date=datetime.fromtimestamp(vacancy["date_published"]).strftime("%d.%m.%Y"),
                    experience=vacancy["experience"]["title"],
                    vacancy_name=vacancy["profession"],
                    salary_min=vacancy["payment_from"],
                    salary_max=vacancy["payment_to"]
                )
            )
        return list_
    except Exception as error:
        raise Exception(f"Ошибка {error}")


def convert_to_json(vacancies: list[Vacancy]) -> list[dict]:
    """
    Конвертирует список экземпляров класса Vacancy в список словарей
    """
    try:
        list_ = []
        for instance in vacancies:
            dict_ = {"id вакансии": instance.vacancy_id, "Должность": instance.vacancy_name,
                     "Ссылка": instance.vacancy_url, "Опыт": instance.experience,
                     "Дата размещения": instance.publication_date, "Зарплата минимальная": instance.salary_min,
                     "Зарплата максимальная": instance.salary_max}
            list_.append(dict_)
        return list_
    except Exception as error:
        raise Exception(f"Ошибка {error}")


def sort_by_date(vacancies: list) -> list:
    """
    Сортирует вакансии по дате
    """
    try:
        for v in vacancies:
            v["Дата размещения"] = datetime.strptime(v["Дата размещения"], "%d.%m.%Y")
        sorted_vacancies = sorted(vacancies, key=lambda x: x["Дата размещения"], reverse=True)
        for v in sorted_vacancies:
            v["Дата размещения"] = v["Дата размещения"].strftime("%d.%m.%Y")
        return sorted_vacancies
    except Exception as error:
        raise Exception(f"Ошибка {error}")


def sort_by_salary(vacancies: list) -> list:
    """
    Сортирует вакансии по зарплате
    """
    try:
        return sorted(vacancies, key=lambda x: x["Зарплата минимальная"], reverse=True)
    except Exception as error:
        raise Exception(f"Ошибка {error}")