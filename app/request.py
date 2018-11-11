from app import app
import urllib.request, json
from .models import news

Sources = news.Sources
Headlines = news.Headlines


#getting api key
api_key = app.config['NEWS_API_KEY']

#getting the base urls
headlines_base_url = app.config["HEADLINES_API_BASE_URL"]
everything_base_url = app.config["EVERYTHING_API_BASE_URL"]
sources_base_url = app.config["SOURCES_API_BASE_URL"]

def get_headlines():
    '''
    Gets the json response to our url request
    '''
    get_headlines_url = headlines_base_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_results(headlines_results_list)

    return headlines_results

def process_results(headlines_list):
        '''
        Processes headlines results and returns a list of objects
        '''
        headlines_results = []
        for headline_item in headlines_list:
                author = headline_item.get('author')
                title = headline_item.get('title')
                description = headline_item.get('description')
                url = headline_item.get('url')
                urlToImage = headline_item.get('urlToImage')
                publishedAt = headline_item.get('publishedAt')
                content = headline_item.get('content')

                if author and urlToImage and content:
                        headlines_object = Headlines(author, title, description, url, urlToImage, publishedAt, content)
                        headlines_results.append(headlines_object)
        return headlines_results
                        
def get_headline():
        get_headline_details_url = headlines_base_url.format(apiKey)
        with urllib.request.urlopen(get_headline_details_url) as url:
                headline_details_data = url.read()
                headline_details_response = json.loads(headline_details_data)

                headline_object = None
                if headline_details_response:
                        author = headline_details_response.get('author')
                        title = headline_details_response.get('title')
                        description = headline_details_response.get('description')
                        url = headline_details_response.get('url')
                        urlToImage = headline_details_response.get('urlToImage')
                        publishedAt = headline_details_response.get('publishedAt')
                        content = headline_details_response.get('content')

                        headline_object = Headlines(author, title, description, url, urlToImage, publishedAt, content)

        return headline_object