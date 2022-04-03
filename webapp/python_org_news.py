from datetime import datetime

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News

from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
<<<<<<< HEAD
=======
            print(published)
>>>>>>> 2d28924be116e0be8960dbceb9c11ed6301da9fb
            try:
                published = datetime.strptime(published, '%B %d, %Y')
            except ValueError:
                published = datetime.now()
<<<<<<< HEAD
            save_news(title=title, url=url, published=published)
    return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
=======
            save_news(title, url, published)


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()

>>>>>>> 2d28924be116e0be8960dbceb9c11ed6301da9fb
