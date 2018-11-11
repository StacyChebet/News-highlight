class Config:
    '''
    Configuration parent class
    '''
    HEADLINES_API_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    EVERYTHING_API_BASE_URL = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    SOURCES_API_BASE_URL = "https://newsapi.org/v2/sources?apiKey={}"
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Developement configuration child class
    '''
    pass

    DEBUG = True