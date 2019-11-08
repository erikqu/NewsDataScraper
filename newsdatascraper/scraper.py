from newspaper import Article
import requests
from models import ArticleFromJson, Articles



class Scraper:
    def __init__(self, api_key: str, mode: str = 'NEWSPAPER'):
        """
        Scraper modes: 
            Newspaper3k => 'NEWSPAPER'
            GNewsAPI => 'GNEWS'
        """
        self.api_key = api_key
        self.mode = mode
        if mode == 'NEWSPAPER':
            self.baseUrl = "https://newsapi.org/v2/everything?"
        elif mode == 'GNEWS':
            self.baseUrl = "https://gnews.io/api/v3/search?"

    def fetch_all_articles(self, query: str, page_size: int = 10) -> Articles:
        """Method to fetch all articles of a specific query.
        Note to get the full body use the get_body method"""
        if self.mode == 'NEWSPAPER':
            url_parameters = "q={0}&pageSize={1}&apiKey={2}".format(
                query, page_size, self.api_key
            )
        elif self.mode == 'GNEWS':
            url_parameters = "q={0}&max={1}&token={2}".format(
                query, page_size, self.api_key
            )
        url = self.baseUrl + url_parameters
        results = requests.get(url).json()
        all_articles = results["articles"]
        return Articles(self.create_article_objects(all_articles))

    def fetch_articles_from_specific_dates(
        self, query: str, date_from: str, date_to: str, page_size: int = 100
    ) -> Articles:
        """Method to fetch articles from specific dates: dates should be in
        format in 2019-08-04"""

        if self.mode == 'NEWSPAPER':
            params = "q={0}&pageSize={1}&apiKey={2}&from={3}&to={4}".format(
                query, page_size, self.api_key, date_from, date_to
            )
        elif self.mode == 'GNEWS': 
            params = "q={0}&max={1}&token={2}&mindate={3}&maxdate={4}".format(
                query, page_size, self.api_key, date_from, date_to
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
            if self.mode == 'NEWSPAPER':
                list_of_articles.append(
                    ArticleFromJson(
                        article["source"]["name"],
                        article["title"],
                        article["description"],
                        article["url"],
                        article["publishedAt"],
                        body,
                        article["author"],
                    )
                )
            elif self.mode == 'GNEWS':
                list_of_articles.append(
                    ArticleFromJson(
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
