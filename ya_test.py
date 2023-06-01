from unittest import TestCase
from yandex_main import add_directory_to_yandex_disk

ya_token = ''
yandex_api_url = "https://cloud-api.yandex.net/"
directory_name = 'Новая папка для тестирования'

class YaApiTestTest(TestCase):
    
    def test_add_directory_to_yandex_disk(self):
        self.assertEqual(add_directory_to_yandex_disk(directory_name, ya_token, yandex_api_url), 201)
        
# if __name__ == '__main__':
#     Tester = YaApiTestTest()
#     Tester.test_add_directory_to_yandex_disk()
    