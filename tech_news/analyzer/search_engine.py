from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    tuples = []
    results = search_news({"title": {'$regex': title, "$options": '-i'}})
    for result in results:
        tuples.append((result["title"], result["url"]))
    return tuples


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
