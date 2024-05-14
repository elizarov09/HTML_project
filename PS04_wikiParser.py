from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def initialize_browser():
    # Настройка браузера
    browser = webdriver.Chrome()
    return browser

def get_article_paragraphs(browser):
    # Получение всех параграфов текущей статьи
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    return paragraphs

def print_paragraphs(paragraphs):
    # Вывод параграфов по одному
    for i, paragraph in enumerate(paragraphs):
        print(f"Paragraph {i + 1}:\n{paragraph.text}\n")
        input("Press Enter to see the next paragraph...")

def get_linked_articles(browser):
    # Получение связанных статей
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    links = []
    for hatnote in hatnotes:
        link_elements = hatnote.find_elements(By.TAG_NAME, "a")
        for link_element in link_elements:
            link = link_element.get_attribute("href")
            if link and "wikipedia.org" in link:
                links.append(link)
    return links

def print_intro():
    print("Welcome to the Wikipedia Console Search Program!")
    print("1. Browse paragraphs of the current article")
    print("2. Go to a linked article")
    print("3. Exit the program")

def browse_article(browser):
    while True:
        paragraphs = get_article_paragraphs(browser)
        print_intro()
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            print_paragraphs(paragraphs)
        elif choice == '2':
            linked_articles = get_linked_articles(browser)
            if linked_articles:
                for i, link in enumerate(linked_articles):
                    print(f"{i + 1}. {link}")
                link_choice = int(input("Choose a linked article (number): ").strip())
                next_link = linked_articles[link_choice - 1]
                browser.get(next_link)
                time.sleep(2)  # Ожидание загрузки страницы
            else:
                print("No linked articles found.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    browser = initialize_browser()

    try:
        # Запрос пользователя на начальный поиск
        initial_query = input("Enter your initial search query: ").strip()
        search_url = f"https://ru.wikipedia.org/wiki/{initial_query}"
        browser.get(search_url)
        time.sleep(2)  # Ожидание загрузки страницы

        browse_article(browser)
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
