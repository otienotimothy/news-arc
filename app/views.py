from flask import render_template
from app import app

from .requests import get_news_sources

@app.route('/')
def home():
    # Render a template for the home route
    news_sources_list = get_news_sources()
    return render_template('index.html', news_list = news_sources_list)
