import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём экземпляр класса Translator
translator = Translator()


# Создаём функцию, которая будет получать информацию и переводить на русский
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        russian_word = translator.translate(english_word, dest='ru').text
        russian_definition = translator.translate(word_definition, dest='ru').text

        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition,
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        russian_word = word_dict.get("russian_word")
        russian_definition = word_dict.get("russian_definition")

        # Начинаем игру
        print(f"Значение слова: {russian_definition}")
        user = input("Что это за слово на английском? ")
        if user.lower() == english_word.lower():
            print("Верно!")
        else:
            print(f"Неверно! Правильный ответ: {russian_word} ({english_word})")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


# Запускаем игру
word_game()
