from src.vacancies import Vacancy


def test_get_vacancy_list(test_file):
    vacancy_num1 = Vacancy.get_vacancies_list(test_file, 'Самара', 40000)
    vacancy_num2 = Vacancy.get_vacancies_list(test_file, 'Пятигорск', 0)
    false_expected = vacancy_num1 < vacancy_num2
    assert false_expected == False
    assert len(vacancy_num1) == 2
    assert len(vacancy_num1[:2]) == 2
