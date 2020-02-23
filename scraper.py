#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

url_to_parse = "https://www.prefeitura.unicamp.br/apps/site/cardapio.php"

def open_url_and_soup_it(url):
    #TODO catch para urllib.error.URLError
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
    return soup

def get_database(url_to_parse):
    return open_url_and_soup_it(url_to_parse)

def parse_meals(meals):
    parsed_meals =[]

    parsed_meals.append([meals[0].get_text()])

    for meal in meals[1:]:
        full_course_dinner = meal.find_all("td")

        parsed_dishes = []
        for dish in full_course_dinner:
            if dish.get_text() == " ":
                continue
            parsed_dishes.append(dish.get_text())
        parsed_meals.append(parsed_dishes)

    return parsed_meals

def split_db_by_meal(db):
    meals = db.find_all(class_="fundo_cardapio")
    meals = parse_meals(meals)

    titles = db.find_all(class_="titulo_cardapio")
    titles = [title.get_text() for title in titles] # filter text
    return zip(titles, meals)

def database_to_dict(database):
    keys = ["breakfast", "lunch", "veg_lunch", "dinner", "veg_dinner"]
    return dict(zip(keys, (split_db_by_meal(database))))

def dump_menu(menu):
    for title, meals in menu:
        print("-" * 80)
        print(title)
        for meal in meals:
            print(meal)

def main():
    database = get_database(url_to_parse)
    menu = split_db_by_meal(database)
    dict = database_to_dict(database)

    print(dict)
    dump_menu(menu)

if __name__ == '__main__':
    main()
