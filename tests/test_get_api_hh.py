from abc import ABC

from src.Abstract_Api_HH import AbstractApiHH
from src.Get_Api_HH import GetApiHH


def test_issubclass():
    assert issubclass(GetApiHH, ABC)
    assert issubclass(GetApiHH, AbstractApiHH)


def test_get_vacancy(fixture_class_get_hh_valid, fixture_class_get_hh_not_valid):
    assert len(fixture_class_get_hh_valid) > 0
    assert fixture_class_get_hh_not_valid == "Вакансия не найдена"


def test_all_vacancy():
    get_api = GetApiHH()
    get_api.get_vacancy("Python")

    assert len(get_api.all_vacancy) > 0
