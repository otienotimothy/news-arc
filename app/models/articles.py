class Article:
    '''
    Define the structure for the news source
    '''

    def __init__(self, source_name, author, title, content, url, img_url, published_at) -> None:
        self.source_name = source_name
        self.author = author
        self.title = title
        self.content = content
        self.url = url
        self.img_url = img_url
        self.published_at = published_at
