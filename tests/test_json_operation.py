from abc import ABC

from src.Abstract_Json_Saver import AbstractJson
from src.Json_operation import JsonOperation


def test_json_operation_issubclass():
    assert issubclass(JsonOperation, AbstractJson)
    assert issubclass(AbstractJson, ABC)


def test_save_file_read_file(fixture_class_json_operation):
    fixture_class_json_operation.file_save([{'name': 'Java'}])

    assert isinstance(fixture_class_json_operation.file_read(), list)
    assert fixture_class_json_operation.file_read() == [{'name': 'Java'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Java'}])

    assert fixture_class_list.file_read() == [{'name': 'Not Java'}, {'name': 'Java'}]

    fixture_class_list.delete_vacancy('Java')
    assert fixture_class_list.file_read() == [{'name': 'Not Java'}]
