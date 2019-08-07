from newspaper import Article
import requests
from .models import ArticleFromJson, Articles


class Scraper:
    def __init__(self, api_key: str):
        self.apiKey = api_key

    def fetch_all_articles(self, query: str, pageSize: int = 100) -> Articles:
        '''Method to fetch all articles of a specific query. Note to get the full body use the get_body method'''
        url = "https://newsapi.org/v2/everything?q={0}&pageSize={1}&apiKey={2}".format(
            query, pageSize, self.apiKey)
        print(url)
        results = requests.get(url).json()
        all_articles = results["articles"]

        return Articles(self.create_article_objects(all_articles))

    def fetch_specific_articles(self, query: str, dateFrom: str, dateTo: str, pageSize: int=100) -> Articles:
        '''Method to fetch specific dates: dates should be in format in 2019-08-04 or 2019-08-04T01:57:12'''
        url = "https://newsapi.org/v2/everything?q={0}&pageSize={1}&apiKey={3}&from={4}&from{5}".format(
            query, pageSize, self.apiKey, dateFrom, dateTo)
        results = requests.get(url).json()
        articles = results["articles"]
        return Articles(self.create_article_objects(articles))

    def create_article_objects(self, articles) -> list:
        '''Method to create a list of article objects'''
        list_of_articles = []
        for article in articles:
            body = self.get_body(article['url'])
            list_of_articles.append(ArticleFromJson(
                article['author'], article['title'], article['description'], article['url'], article['publishedAt'], body))
        return list_of_articles

    def get_body(self, url: str) -> str:
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text
        except:
            return 'Could not retrieve body at this time'
