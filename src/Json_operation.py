import json
from config import PATH_TO_JSON_DATA
from src.Abstract_Json_Saver import AbstractJson


class JsonOperation(AbstractJson):
    def file_save(self, data: list):
        """Сохраняем json-файл"""
        with open(PATH_TO_JSON_DATA, 'w', encoding='cp1251') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    def file_read(self):
        """Чтение json-файла"""
        with open(PATH_TO_JSON_DATA, encoding='cp1251') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data: list):
        """Добавление вакансий в файл"""
        old_list = self.file_read()
        new_list = data + old_list
        self.file_save(new_list)

    def delete_vacancy(self, vacancy: str):
        new_list = []

        old_list = self.file_read()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.file_save(new_list)
