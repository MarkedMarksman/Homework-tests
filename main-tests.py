from main import exercise_1,exercise_2,exercise_3
from unittest import TestCase

class MyTest(TestCase):
    def test_exercise_1(self):
        geo_logs_russia = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']},
            {'visit11':['Киров','Россия']},
        ]
        self.assertListEqual(exercise_1(),geo_logs_russia)
        
    def test_exercise_2(self):
        ids_result = [98, 35, 15, 213, 54, 119]  
        self.assertListEqual(exercise_2(),ids_result)

    def test_exercise_3(self):
        queries = [
            'смотреть сериалы онлайн', 'новости спорта кино театра', 'афиша',
            'курс доллара', 'сериалы этим летом', 'курс по питону огромной змее',
            'сериалы про спорт'
            ]
        queries_result = f'Поисковых запросов из 3 слова 42.86% кол-во запросов 3\nПоисковых запросов из 4 слова 14.29% кол-во запросов 1\nПоисковых запросов из 1 слова 14.29% кол-во запросов 1\nПоисковых запросов из 2 слова 14.29% кол-во запросов 1\nПоисковых запросов из 5 слова 14.29% кол-во запросов 1\n'
        
        self.assertEqual(exercise_3(),queries_result)
    
# if __name__ == '__main__':
#     Tester = MyTest()
#     Tester.test_exercise_1()
#     Tester.test_exercise_2()
#     Tester.test_exercise_3()