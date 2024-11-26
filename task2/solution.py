import requests
from bs4 import BeautifulSoup
import csv


def count_animals(base_url: str, animals_count: dict) -> dict:
    next_page = True
    url = base_url

    while next_page:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        ru_content = soup.find("div", lang="ru", class_="mw-category-generated")
        pages = ru_content.find("div", id="mw-pages")

        if pages:
            columns = pages.find_all("div", class_="mw-category-group")

        for group in columns:
            letter = group.find("h3").text
            animals = group.find_all("li")
            if letter in animals_count:
                animals_count[letter] = animals_count.get(letter, 0) + len(animals)

        next_page_link = soup.find("a", string="Следующая страница")
        if next_page_link:
            url = "https://ru.wikipedia.org" + next_page_link["href"]
        else:
            next_page = False

    return animals_count


def write_to_csv_file(data: dict, path: str = "task2/beasts.csv") -> None:
    with open(path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for letter, count in data.items():
            writer.writerow([letter, count])

        print("Данные успешно записаны в файл beasts.csv")


base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
animals_dict = {letter: 0 for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"}

animals_count = count_animals(base_url, animals_dict)
write_to_csv_file(animals_count)
