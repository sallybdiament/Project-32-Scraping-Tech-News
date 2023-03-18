from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 7
def search_by_title(title):
    tuples = []
    results = search_news({"title": {'$regex': title, "$options": '-i'}})
    for result in results:
        tuples.append((result["title"], result["url"]))
    return tuples


# Requisito 8
def search_by_date(date):
    try:
        mat = re.match('(\\d{2})[/.-](\\d{2})[/.-](\\d{4})$', date)
        if mat is not None:
            tuples = []
            correct = datetime.strptime(date, "%d/%m/%Y").strftime('%Y-%m-%d')
            results = search_news({"timestamp": correct})
            for result in results:
                tuples.append((result["timestamp"], result["url"]))
        return tuples
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    tuples = []
    results = search_news({"category": {'$regex': category, "$options": '-i'}})
    for result in results:
        tuples.append((result["title"], result["url"]))
    return tuples
