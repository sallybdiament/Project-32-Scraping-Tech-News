import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news = selector.css('h2.entry-title a::attr(href)').getall()
    if(len(news) == 0):
        return []
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    d = {}
    read_time = selector.css('li.meta-reading-time::text').get()
    if read_time[1].isdigit():
        minutos = int(read_time[0] + read_time[1])
    else:
        minutos = int(read_time[0])
    d['url'] = selector.css("link[rel='canonical']::attr(href)").get().strip()
    d['title'] = selector.css('h1.entry-title::text').get().strip()
    d['timestamp'] = selector.css('li.meta-date::text').get()
    d['writer'] = selector.css('a.url.fn.n::text').get().strip()
    d['reading_time'] = int(minutos)
    d['summary'] = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall()
    ).strip()
    d['category'] = selector.css('div.meta-category span.label::text').get()
    return d


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    documents = []
    while len(documents) < amount:
        page_content = fetch(url)
        link_news = scrape_updates(page_content)
        for link in link_news:
            if len(documents) < amount:
                documents.append(scrape_news(fetch(link)))
            else:
                break
        url = scrape_next_page_link(page_content)
    create_news(documents)
    return documents
