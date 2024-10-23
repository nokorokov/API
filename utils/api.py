import json

import requests

from utils.http_methods import HttpMethods

"""Методы для тестирования GMA"""

base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'     # Параметр для всех запросов


class GoogleMapsApi:

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        post_resource = '/maps/api/place/add/json'   # Путь метода POST

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.json())

        return result_post

    """Метод для получения новой локации"""
    @staticmethod
    def get_new_place(place_id):
        get_resource = '/maps/api/place/get/json'  # Путь метода GET

        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = '/maps/api/place/update/json'  # Путь метода PUT

        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_place = {
                "place_id": place_id,
                "address": "100 Lenina street, RU",
                "key": "qaclick123"
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        print(result_put.json())
        return result_put

    """Метод для удаления новой локации"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = '/maps/api/place/delete/json'  # Путь метода DELETE

        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_place = {
            "place_id": place_id
        }

        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_place)
        print(result_delete.json())
        return result_delete

    def testst(self):
        url = "https://dog.ceo/api/breed/hound/images"
        result = requests.get(url)
        result_json = result.json()
        result_json2 = 0
        if 'message' in result_json:
            for image_url in result_json['message']:
                if 'hound-english' in image_url:
                    result_json2 += 1
        print(result_json2)

rewtw = GoogleMapsApi()
rewtw.testst()





