from flask import render_template
from app import app
from .request import get_headlines, get_article

#Views
@app.route ('/')
def index():
    '''
    Returns index page and its data
    '''

    #Getting headlines
    news_headlines = get_headlines()
    print (news_headlines)
    title = 'News Highlight- Fast and reliable way to get news'
    return render_template('index.html', title = title, headlines = news_headlines)