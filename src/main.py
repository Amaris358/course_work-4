from pprint import pprint

from classes.HHClass import HeadHunterAPI
from classes.SaverClass import SaverJSON
from classes.SJCalss import SuperJobAPI
from src.funcs import (
    convert_to_json,
    get_hh_vacancies,
    get_sj_vacancies,
    sort_by_date,
    sort_by_salary,
)


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input(
        """Введите поисковый запрос:
    (Запрос может содержать более одного слова - вводятся через пробел)
    ->>> """
    )
    platforms = input(
        """Выберите платформу для поиска вакансий:
        hh - HeadHunter;
        sj - SuperJob;
        По умолчанию - HeadHunter и SuperJob;
    ->>> """
    )
    try:
        if platforms.lower() == "hh":
            hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API HH
            hh_vacancies = hh_api.get_vacancies(search_query)  # Получение вакансий с HH
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_hh_vacancies(hh_vacancies)

        elif platforms.lower() == "sj":
            superjob_api = SuperJobAPI()  # Создание экземпляра класса для работы с API SJ
            superjob_vacancies = superjob_api.get_vacancies(search_query)  # Получение вакансий с SJ
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_sj_vacancies(superjob_vacancies)

        else:
            # Создание экземпляра класса для работы с API сайтов с вакансиями
            hh_api = HeadHunterAPI()
            superjob_api = SuperJobAPI()
            # Получение вакансий с разных платформ
            hh_vacancies = hh_api.get_vacancies(search_query)
            superjob_vacancies = superjob_api.get_vacancies(search_query)
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_hh_vacancies(hh_vacancies) + get_sj_vacancies(
                superjob_vacancies
            )
    except Exception:
        raise Exception

    if not all_instances_list:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # Преобразование списка экземпляров класса Vacancy в json формат
    vacancies_json_list = convert_to_json(all_instances_list)
    print(f"Найдено {len(vacancies_json_list)} вакансий.")

    # Сохранение списка вакансий в файл
    json_saver = SaverJSON()
    json_saver.add_vacancies(vacancies_json_list)

    output_choice = input(
        """Введите желаемый вариант вывода:
    date - Для вывода вакансий по дате;
    salary - Для вывода вакансий по зарплате;
    both - Для вывода вакансий по зарплате и по дате;
    По умолчанию - вывод всех вакансий отфильтрованных по дате
    ->>> """
    )

    if output_choice.lower() == "date":
        user_number_input = input("Введите количество вакансий для вывода ")
        try:
            pprint(sort_by_date(vacancies_json_list)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return

    elif output_choice.lower() == "salary":
        try:
            salary_input = input("Введите нижний и верхний порог зарплаты через пробел ")
            from_ = salary_input.split(" ")[0]
            to_ = salary_input.split(" ")[1]
            choisen_vacancies = json_saver.get_by_salary(int(from_), int(to_))
            user_number_input = input("Введите количество вакансий для вывода ")
            pprint(sort_by_salary(choisen_vacancies)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return

    elif output_choice.lower() == "both":
        try:
            salary_input = input("Введите нижний и верхний порог зарплаты через пробел ")
            from_ = salary_input.split(" ")[0]
            to_ = salary_input.split(" ")[1]
            choisen_vacancies = json_saver.get_by_salary(int(from_), int(to_))
            user_number_input = input("Введите количество вакансий для вывода ")
            pprint(sort_by_date(choisen_vacancies)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return
    else:
        pprint(sort_by_date(vacancies_json_list))


user_interaction()
