import unittest
from app.models import Headlines, Sources

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    ''' 
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headline = Headline('Stacy Chebet','Kyrsten Sinema Declared War Winner','Ms. Sinema scored a ground breaking victory','www.news.com','www.sinema123.com', '2018-9-12-13T00:50:04Z', 'If one of the biggest themes...' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Headline))


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news','www.abcnews.com','general', 'en', 'us' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

