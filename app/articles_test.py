import unittest
from models.articles import Article


class News_sourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Antaranews.com', "Mansyur suryana", "145 warga Lebak-Banten terserang DBD, empat meninggal - ANTARA",
                                   "Selasa, 1 Maret 2022 13:05 WIB\r\nKantor Dinas Kesehat", "https://www.antaranews.com/berita/2732549/145-warga-lebak-banten-terserang-dbd-empat-meninggal", "https://img.antaranews.com/cache/800x533/2022/03/01/IMG_20220203_152900.jpg")

    def test_instance(self):
        '''
        Test that the instance created was created from the News_Source class
        '''
        self.assertTrue(isinstance(self.new_article, Article))

    def test_attr(self):
        '''
        Test that the instance were created correctly
        '''
        self.assertEqual(self.news_source.name, 'Antaranews.com')
        self.assertEqual(self.news_source.author, "Mansyur suryana")
        self.assertEqual(self.news_source.title,
                         "145 warga Lebak-Banten terserang DBD, empat meninggal - ANTARA")
        self.assertEqual(self.news_source.content,
                         "Selasa, 1 Maret 2022 13:05 WIB\r\nKantor Dinas Kesehat")
        self.assertEqual(
            self.news_source.url, "https://www.antaranews.com/berita/2732549/145-warga-lebak-banten-terserang-dbd-empat-meninggal")
        self.assertEqual(self.news_source.img_url,
                         "https://img.antaranews.com/cache/800x533/2022/03/01/IMG_20220203_152900.jpg")
        self.assertEqual(self.news_source.published_at, "2022-03-01T06:05:43Z")


if __name__ == '__main__':
    unittest.main()
