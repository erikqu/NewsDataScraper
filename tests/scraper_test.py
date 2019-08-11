import sys
import os
#Needs access to the package newspaper
TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

import requests
import json
from newsdatascraper import Scraper
from newsdatascraper.models import Articles, ArticleFromJson
from httmock import urlmatch, HTTMock, response, all_requests
from unittest.mock import MagicMock

news_api_mock_data = {
    'status': 'ok',
    'totalResults': 1,
    'articles': [
        {
            'source': {
                'id': '',
                'name': 'Darkreading.com'
            },
            'author': 'Joe',
            'title': 'Mock',
            'description': 'Mock',
            'url': 'www.mock.com',
            'urlToImage': 'www.mock.image',
            'publishedAt': '2019-08-11T01:05:00Z',
            'content': 'mock-content'
        }
    ]
}

article_object = ArticleFromJson(
    'Joe', 'Mock', 'Mock', 'www.mock.com', '2019-08-11T01:05:00Z', 'content_went_to_body')
mock_articles_object = Articles([article_object])


class TestScraperMethods:

    @all_requests
    def news_api_mock(self, url, request):
        headers = {'content-type': 'application/json',
                   'Set-Cookie': 'foo=bar;'}
        return response(200, news_api_mock_data, headers, None, 1, request)

    def test_fetch_all_articles(self):
        scraper = Scraper('mock-url')
        scraper.get_body = MagicMock(return_value='content_went_to_body')
        with HTTMock(self.news_api_mock):
            articles_object = scraper.fetch_all_articles(query='mock')
        
        assert mock_articles_object.articles[0].content != news_api_mock_data['articles'][0]['content']
        assert mock_articles_object == articles_object

    def test_fetch_all_articles(self):
        scraper = Scraper('mock-url')
        scraper.get_body = MagicMock(return_value='content_went_to_body')
        with HTTMock(self.news_api_mock):
            articles_object = scraper.fetch_articles_from_specific_dates(query='mock', dateFrom='mock-date', dateTo='mock-date')
        assert mock_articles_object.articles[0].content != news_api_mock_data['articles'][0]['content']
        assert mock_articles_object == articles_object
