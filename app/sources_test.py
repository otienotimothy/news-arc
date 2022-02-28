import unittest
from models.sources import News_Source


class News_sourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_source = News_Source("abc-news", "ABC News", 'Your trusted source for breaking news and analysis',
                                       "en", "https://abcnews.go.com",  "us")

    def test_instance(self):
        '''
        Test that the instance created was created from the News_Source class
        '''
        self.assertTrue(isinstance(self.news_source, News_Source))

    def test_attr(self):
        '''
        Test that the instance were created correctly
        '''
        self.assertEqual(self.news_source.id, "abc-news")
        self.assertEqual(self.news_source.name, "ABC News")
        self.assertEqual(self.news_source.description,
                         'Your trusted source for breaking news and analysis')
        self.assertEqual(self.news_source.language, "en")
        self.assertEqual(self.news_source.url, "https://abcnews.go.com")
        self.assertEqual(self.news_source.country, "us")



if __name__ == '__main__':
    unittest.main()