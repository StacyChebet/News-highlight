from flask import render_template
from . import main
from ..request import get_headlines, get_headline, get_sources, get_sources_articles

#Views
@main.route ('/')
def index():
    '''
    Returns index page and its data
    '''

    #Getting headlines
    news_headlines = get_headlines()
    title = 'News Highlight- Fast and reliable way to get news'
    return render_template('index.html', title = title, headlines = news_headlines)

@main.route ('/headlines/title')
def headlines(title):
    '''
    View headlines page function that returns headlines details page and its data
    '''
    headline = get_article(title)
    title = f'{article.title}'

    return render_template('headlines.html', title = title, headline = headline)

@main.route ('/sources/<category>')
def sources(category):
    sources = get_sources(category)
    title = category
    return render_template('sources.html', sources = sources, title = title)

@main.route("/sources_articles/articles/<id>")
def source_articles(id):
    """
    View function for a specific source's articles
    """
    articles = get_sources_articles(id)
    title = id
    return render_template("source_articles.html", articles = articles, title=title)

