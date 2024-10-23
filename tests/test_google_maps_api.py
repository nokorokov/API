from utils.api import GoogleMapsApi
from utils.cheking import Checking
import allure

"""Создание  изменение и удаление новой локации"""


@allure.epic('Тест по созданию новой локации')
class TestCreatePlace:
    """Класс содержащий тест по работе с локацией"""

    @allure.description('Создание изменение удаление новой локации')
    def test_create_new_place(self):
        """Тест по созданию, изменение и удаление новой локации"""

        print('\nМетод POST')
        result_post = GoogleMapsApi.create_new_place()
        Checking.check_status_code(result_post, 200)
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('\nМетод GET -> POST')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name',
                                               'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('\nМетод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('\nМетод GET -> PUT')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('\nМетод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('\nМетод GET -> DELETE')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        print(result_get.json())
        Checking.check_json_value(result_get, 'msg',
                                  "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print('\nТестирование создания, изменения и удаления новой локации прошло успешно')
