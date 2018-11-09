from flask import render_template
from app import app

#Views
@app.route ('/')
def index():
    '''
    Returns index page and its data
    '''
    title = 'News Highlight'
    return render_template('index.html', title = title)