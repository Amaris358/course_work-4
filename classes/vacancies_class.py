class Vacancy:
    """

    """
    def __init__(self,
                 vacancy_id,
                 vacancy_url,
                 publication_date,
                 experience,
                 vacancy_name,
                 salary_min,
                 salary_max
                 ):
        self.vacancy_id = vacancy_id
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.publication_date = publication_date
        self.experience = experience
        self.salary_min = salary_min
        self.salary_max = salary_max
