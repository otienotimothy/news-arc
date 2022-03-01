from flask import render_template
from app import app

from .requests import get_news_sources, get_top_headlines

@app.route('/')
def home():
    # Render a template for the home route
    news_sources_list = get_news_sources()
    return render_template('index.html', news_list = news_sources_list)

@app.route('/headlines/<source>')
def articles(source):
    # Render template for the Top Articles
    top_articles = get_top_headlines(source)
    return render_template('articles.html', title = source, top_articles = top_articles)
