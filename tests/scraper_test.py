from newsdatascraper import Scraper
from newsdatascraper.models import Articles, ArticleFromJson
from httmock import HTTMock, response, all_requests
from unittest.mock import MagicMock

news_api_mock_data = {
    "status": "ok",
    "totalResults": 1,
    "articles": [
        {
            "source": {"id": "", "name": "Darkreading.com"},
            "author": "Joe",
            "title": "Mock",
            "description": "Mock",
            "url": "www.mock.com",
            "urlToImage": "www.mock.image",
            "publishedAt": "2019-08-11T01:05:00Z",
            "content": "mock-content",
        }
    ],
}

article_object = ArticleFromJson(
    "Joe",
    "Darkreading.com",
    "Mock",
    "Mock",
    "www.mock.com",
    "2019-08-11T01:05:00Z",
    "content_went_to_body",
)
mock_articles_object = Articles([article_object])


class TestScraperMethods:
    @all_requests
    def news_api_mock(self, url, request):
        headers = {"content-type": "application/json"}
        return response(200, news_api_mock_data, headers, None, 1, request)

    def test_fetch_all_articles(self):
        scraper = Scraper("mock-url")
        scraper.get_body = MagicMock(return_value="content_went_to_body")
        with HTTMock(self.news_api_mock):
            articles_object = scraper.fetch_all_articles(query="mock")

        assert (
            articles_object.articles[0].content
            != news_api_mock_data["articles"][0]["content"]
        )
        assert mock_articles_object == articles_object

    def test_fetch_articles_from_specific_dates(self):
        scraper = Scraper("mock-url")
        scraper.get_body = MagicMock(return_value="content_went_to_body")
        with HTTMock(self.news_api_mock):
            articles_object = scraper.fetch_articles_from_specific_dates(
                query="mock", dateFrom="mock-date", dateTo="mock-date"
            )
        assert (
            articles_object.articles[0].content
            != news_api_mock_data["articles"][0]["content"]
        )
        assert mock_articles_object == articles_object

    def test_get_body_fails_and_returns(self):
        scraper = Scraper("mock-url")
        content = scraper.get_body("www.mock-website.com")
        assert content == "Could not retrieve body at this time"
