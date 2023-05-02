from bs4 import BeautifulSoup
import requests

def get_items():
    url = 'https://steamcommunity.com/id/nik4ez/inventory/#730'
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('h1', class_='hover_item_name')
    print(items)

def main():
    get_items()

if __name__ == '__main__':
    main()
