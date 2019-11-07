from newspaper import Article
import requests
from .models import ArticleFromJson, Articles


class Scraper:
    def __init__(self, api_key: str):
        self.apiKey = api_key
        self.baseUrl = "https://newsapi.org/v2/everything?"

    def fetch_all_articles(self, query: str, pageSize: int = 100) -> Articles:
        """Method to fetch all articles of a specific query.
        Note to get the full body use the get_body method"""
        url_parameters = "q={0}&pageSize={1}&apiKey={2}".format(
            query, pageSize, self.apiKey
        )
        url = self.baseUrl + url_parameters
        results = requests.get(url).json()
        all_articles = results["articles"]
        return Articles(self.create_article_objects(all_articles))

    def fetch_articles_from_specific_dates(
        self, query: str, dateFrom: str, dateTo: str, pageSize: int = 100
    ) -> Articles:
        """Method to fetch articles from specific dates: dates should be in
        format in 2019-08-04 or 2019-08-04T01:57:12"""
        params = "q={0}&pageSize={1}&apiKey={2}&from={3}&to={4}".format(
            query, pageSize, self.apiKey, dateFrom, dateTo
        )
        url = self.baseUrl + params
        results = requests.get(url).json()
        try:
            articles = results["articles"]
        except KeyError:
            return Articles([])
        return Articles(self.create_article_objects(articles))

    def create_article_objects(self, articles) -> list:
        """Helper method to create a list of article objects"""
        list_of_articles = []
        for article in articles:
            body = self.get_body(article["url"])
            list_of_articles.append(
                ArticleFromJson(
                    article["author"],
                    article["source"]["name"],
                    article["title"],
                    article["description"],
                    article["url"],
                    article["publishedAt"],
                    body,
                )
            )
        return list_of_articles

    def get_body(self, url: str) -> str:
        """Helper method to get the body of a article from its url"""
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text  # pragma: no cover
        except Exception:
            return "Could not retrieve body at this time"
