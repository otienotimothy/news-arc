from app import app
import urllib.request, json

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