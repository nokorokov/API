"""Методы для проверки ответов наших запросов"""
import json


class Checking:
    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    """Метод для проверки обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print('Все поля присутствуют')

    """Метод для проверки значения поля"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = json.loads(result.text)
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Значение поля {field_name} - корректно')

    """Метод для проверки значения поля по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = json.loads(result.text)
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Слово {search_word} присутствует в ответе')
        else:
            print(f'Слово {search_word} отсутствует в ответе')


