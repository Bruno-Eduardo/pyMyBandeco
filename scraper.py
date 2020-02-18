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
def main():
    database = get_database(url_to_parse)
if __name__ == '__main__':
    main()
