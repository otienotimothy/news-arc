
import urllib.request
import json
from app.models import Article, News_Source

# Getting the API KEY
# api_key = app.config['API_KEY']
api_key = None
NEWS_SOURCES_BASE_URL = None
TOP_HEADLINES_URL = None
SEARCH_BY_CATEGORY_URL = None


# Set configurable objects
def configure_request(app):
    global api_key, NEWS_SOURCES_BASE_URL, TOP_HEADLINES_URL, SEARCH_BY_CATEGORY_URL
    api_key = app.config['API_KEY']
    NEWS_SOURCES_BASE_URL = app.config['NEWS_SOURCES_BASE_URL']
    TOP_HEADLINES_URL = app.config['TOP_HEADLINES_URL']
    SEARCH_BY_CATEGORY_URL = app.config['SEARCH_BY_CATEGORY_URL']




# GET NEWS SOURCES
def get_news_sources():
    '''
    Function to Fetch a list of News Sources
    '''
    sources_url = NEWS_SOURCES_BASE_URL

    news_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(news_sources_url) as url:
        res = url.read()
        data = json.loads(res)

        news_sources = None

        if data['sources']:
            news_sources_list = data['sources']
            news_sources = format_data(news_sources_list)

    return news_sources


def format_data(news_list):
    '''
    Format the fetched news data as configured in the class blueprint
    '''

    news = []

    for news_item in news_list:
        source_id = news_item['id']
        source_name = news_item['name']
        source_description = news_item['description']
        source_language = news_item['language']
        source_url = news_item['url']
        source_country = news_item['country']

        news_data = News_Source(
            source_id, source_name, source_description, source_language, source_url, source_country)

        news.append(news_data)

    return news

def get_top_headlines(source):
    '''
    Fetch News headlines based on a specified source
    '''
    top_headlines_base_url = TOP_HEADLINES_URL
    headlines_url = top_headlines_base_url.format(source, api_key)

    with urllib.request.urlopen(headlines_url) as url:
        res = url.read()
        data = json.loads(res)

        top_headlines = None

        if data['totalResults']:
            headline_list = data['articles']
            top_headlines = format_articles(headline_list)

    return top_headlines


def get_articles_by_category(source):
    '''
    Fetch News headlines based on a specified source
    '''
    category_base_url = SEARCH_BY_CATEGORY_URL
    category_url = category_base_url.format(source, api_key)

    with urllib.request.urlopen(category_url) as url:
        res = url.read()
        data = json.loads(res)

        top_headlines = None

        if data['totalResults']:
            headline_list = data['articles']
            top_headlines = format_articles(headline_list)

    return top_headlines if top_headlines else []



def format_articles(articles_list):
    '''
    Format the fetched news Articles as configured in the class Article blueprint
    '''

    top_articles = []

    for article_item in articles_list:
        source_name = article_item['source']['name']
        author = article_item['author']
        title = article_item['title']
        content = article_item['content']
        url = article_item['url']
        img_url = article_item['urlToImage']
        published = article_item['publishedAt']

        article_data = Article(source_name, author, title, content, url, img_url, published)

        top_articles.append(article_data)

    return top_articles