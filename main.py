# Задание 1
def exercise_1():
    geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']},
    {'visit11':['Киров','Россия']},
    {'visit12':['Анталья','Турция']}
    ]
    ru_visits = []
    for visits in geo_logs:
        for visit in visits:
            for key,value in visits.items():
                if "Россия" in value:
                    geo_logs = visits 
                    ru_visits.append(geo_logs)
    return ru_visits   
#Задание 2
def exercise_2():
    ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]
        }
    
    all_ids = list(ids.values())
    geo_ids = list(all_ids[0]) + list(all_ids[1]) +list(all_ids[2])
    un_ids = set(geo_ids)
    unique_ids = list(un_ids)
    return unique_ids
# #Задание 3
def exercise_3():
    queries = [
        'смотреть сериалы онлайн', 'новости спорта кино театра', 'афиша',
        'курс доллара', 'сериалы этим летом', 'курс по питону огромной змее',
        'сериалы про спорт'
        ]
    words_count = {}
    newline = '\n'
    result = ''
    for q in queries:
        length = len(q.split(' '))
        words_count[length] = words_count.get(length, 0) + 1
    for k, v in words_count.items():
        percent = v / sum(words_count.values()) * 100
        r = round((percent),2)
        result += (f"Поисковых запросов из {k} слова {r}% кол-во запросов {v}{newline}")
    return result 

