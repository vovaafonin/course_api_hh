from src.Get_Api_HH import GetApiHH
from src.Json_operation import JsonOperation
from src.vacancies import Vacancy

if __name__ == '__main__':

    response = GetApiHH()

    while True:
        user_vacancy: str = input("Напишите название вакансии, которую хотите найти:\n")
        user_city: str = input("Напишите город, в котором хотите найти вакансии:\n")
        if isinstance(user_city, str) and isinstance(user_vacancy, str):
            break

    while True:
        user_salary = input("Напишите минимальную зарплату:\n")
        if user_salary.isdigit():
            break
        print("Попробуйте написать цифрами.")

    # Получаем вакансию для пользователя
    response.get_vacancy(user_vacancy)

    file_json = JsonOperation()

    # Сохраняем результат в JSON файл
    file_json.file_save(response.all_vacancy)

    # Читаем JSON файл
    file_vacancies = file_json.file_read()

    # Сортируем и выводим вакансии ползователю
    vacancy = Vacancy.get_vacancies_list(file_vacancies, user_city, int(user_salary))
    sorted_vacancies = sorted(vacancy)

    while True:
        count = input("Какое кол-во вакансий вы хотите видеть?:\n")
        if count.isdigit():
            break
        print("Попробуйте написать цифрами.")

    print(*sorted_vacancies[:int(count)])
