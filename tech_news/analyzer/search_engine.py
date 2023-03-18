from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    t2 = '/' + str(title) + '/i'
    tuples = []
    results = search_news({"title": {'$regex': f'^{t2}$', "$options": '-i'}})
    for result in results:
        tuples.append((result["title"], result["url"]))
    return tuples


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
