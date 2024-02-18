import pytest
import json
from config import PATH_TO_JSON_TEST
from src.Get_Api_HH import GetApiHH
from src.Json_operation import JsonOperation


@pytest.fixture
def test_file():
    with open(PATH_TO_JSON_TEST, encoding="cp1251") as file:
        return json.load(file)


@pytest.fixture
def fixture_class_list():
    save_operation = JsonOperation()
    save_operation.file_save([{'name': 'Java'}])
    return save_operation


@pytest.fixture
def fixture_class_json_operation():
    return JsonOperation()


@pytest.fixture
def fixture_class_get_hh_valid():
    return GetApiHH().get_vacancy("Python")


@pytest.fixture
def fixture_class_get_hh_not_valid():
    return GetApiHH().get_vacancy("5")
