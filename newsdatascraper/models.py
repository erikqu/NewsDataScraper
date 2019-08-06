from datetime import date


class ArticleFromJson:
   def __init__(self, author: str, title: str, description: str, url: str, datePublished, content: str):
       self.author = author
       self.title = title
       self.description = description
       self.url = url
       self.datePublished = datePublished
       self.content = content

class Articles:
    def __init__(self, articles : list):
        self.articles = articles
