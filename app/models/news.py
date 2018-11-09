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