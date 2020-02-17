from bs4 import BeautifulSoup
from urllib.request import urlopen

url_to_parse = "https://www.amazon.com.br"

def open_url_and_soup_it(url):
    #TODO catch para urllib.error.URLError
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
    return soup

if __name__ == '__main__':
    print(open_url_and_soup_it(url_to_parse))