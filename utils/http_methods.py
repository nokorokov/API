import allure
import requests
from utils.logger import Logger

"""Список HTTP методов"""


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step('Получение данных'):
            Logger.add_request_data_to_log(url, method='GET')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response_data_to_log(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('Создание данных'):
            Logger.add_request_data_to_log(url, method='POST')
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response_data_to_log(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('Изменение данных'):
            Logger.add_request_data_to_log(url, method='PUT')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response_data_to_log(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step('Удаление данных'):
            Logger.add_request_data_to_log(url, method='DELETE')
            result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response_data_to_log(result)
            return result
    