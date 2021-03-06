import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?category=general&language=en&country=us&apiKey={}'

    TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&from=2022-02-28&sortBy=popularity&apiKey={}'

    SEARCH_BY_CATEGORY_URL = 'https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey={}'

    API_KEY = os.environ.get('API_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}