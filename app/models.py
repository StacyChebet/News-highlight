class Headlines:
    '''
    Defines new News objects
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt 
        self.content = content

class Sources:
    '''
    Defines new Sources objects
    '''

    def __init__(self, source_id, name, description, url, category, language, country):
        self.source_id = source_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country