import requests

# URL для отправки GET-запроса с параметрами фильтрации
url = 'https://jsonplaceholder.typicode.com/posts'

# Параметры запроса: фильтр по userId=1
params = {'userId': 1}

# Отправляем GET-запрос с параметрами фильтрации
response = requests.get(url, params=params)

# Проверяем успешность запроса
if response.status_code == 200:
    # Распечатываем полученные записи
    print('Полученные записи:')
    for post in response.json():
        print(post)
else:
    print('Ошибка при выполнении запроса:', response.status_code)
