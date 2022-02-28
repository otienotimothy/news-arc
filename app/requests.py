from app import app
import urllib.request
import json
from .models import sources

# Getting the API KEY
api_key = app.config['API_KEY']

# GET NEWS SOURCES


def get_news_sources():
    '''
    Function to Fetch a list of News Sources
    '''
    sources_url = app.config['NEWS_SOURCES_BASE_URL']

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

        news_data = sources.News_Source(
            source_id, source_name, source_description, source_language, source_url, source_country)

        news.append(news_data)

    return news
