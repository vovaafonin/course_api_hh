import json
import requests
from src.Abstract_Api_HH import AbstractApiHH


class GetApiHH(AbstractApiHH):
    def __init__(self):
        self.all_vacancy = []

    def get_vacancy(self, name_vacancy) -> list:
        """Получаем информацию о вакансиях для пользователя"""

        if name_vacancy.isalpha():
            keys_response = {'text': f'NAME:{name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            self.all_vacancy = json.loads(info.text)['items']
            return self.all_vacancy
        else:
            return "Вакансия не найдена"
