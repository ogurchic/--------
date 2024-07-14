import requests
from bs4 import BeautifulSoup
import webbrowser as wb

url = 'https://habr.com/ru/articles/'

def read_news():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    art = soup.find_all('h2', class_='tm-title tm-title_h2')

    k = 0
    news = []
    for i in art:
        k+=1
        if k < 6:
            title = i.a.span.text
            news.append(title)
        else: break
    return news

def open_news():
    wb.open(url)