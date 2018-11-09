class Config:
    '''
    Configuration parent class
    '''
    NEWS_API_BASE_URL = "https://newsapi.org/v2/everything/{}?api_key = {}"

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