from flask import render_template
from app import app

from .requests import get_news_sources, get_top_headlines, get_articles_by_category

@app.route('/')
def home():
    # Render a template for the home route
    news_sources_list = get_news_sources()
    return render_template('index.html', news_list = news_sources_list)

@app.route('/<category>')
def category(category):
    # Render Article of a certain Category
    category_list = get_articles_by_category(category)
    print(category_list)
    return render_template('articles.html', title=category, top_articles=category_list)

@app.route('/headlines/<source>')
def articles(source):
    # Render template for the Top Articles
    top_articles = get_top_headlines(source)
    return render_template('articles.html', title = source, top_articles = top_articles)
