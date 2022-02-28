class News_Source:
    '''
    Define the structure for the news source
    '''

    def __init__(self, id, name, description, language, url, country) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.url = url
        self.country = country