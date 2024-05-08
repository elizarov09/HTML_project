import requests
import pprint

# URL открытого API для поиска репозиториев на GitHub
url = 'https://api.github.com/search/repositories'

# Параметры запроса: искать репозитории с кодом html
params = {'q': 'html'}

# Отправляем GET-запрос к API GitHub
response = requests.get(url, params=params)

# Распечатываем статус-код ответа
print('Статус-код ответа:', response.status_code)

# Красиво выводим содержимое ответа в формате JSON
print('Содержимое ответа (JSON):')
pprint.pprint(response.json())
