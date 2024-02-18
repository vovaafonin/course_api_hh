class Vacancy:
    vacancies_list = []

    def __init__(self, name_vacancy: str, salary_from: int, salary_to: int, url: str, city: str):
        self.name_vacancy = name_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.city = city
        self.vacancies_list.append(self)

    def __repr__(self):
        return (f"\nНазвание: {self.name_vacancy}\n"
                f"Зарплата от: {self.salary_from}\n"
                f"Зарплата до: {self.salary_to}\n"
                f"В городе: {self.city}\n"
                f"URL: {self.url}\n")

    def __lt__(self, other):
        if other.salary_to < self.salary_to:
            return True

    @classmethod
    def get_vacancies_list(cls, vacancies_list, city, salary_from) -> list:
        """ Получаем список с вакансиями."""
        for vacancy in vacancies_list:
            name_vacancy = vacancy["name"]
            url = vacancy["alternate_url"]
            if vacancy["area"]["name"] == city:
                city = vacancy["area"]["name"]
            if vacancy["salary"] is None:
                continue
            elif vacancy["salary"]["to"] is not None and vacancy["salary"]["from"]:
                if vacancy["salary"]["from"] >= salary_from:
                    salary_from = vacancy["salary"]["from"]
                    salary_to = vacancy["salary"]["to"]
                    cls(name_vacancy, salary_from, salary_to, url, city)
                else:
                    continue
            else:
                continue
        return cls.vacancies_list
