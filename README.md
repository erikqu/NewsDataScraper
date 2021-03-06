# NewsDataScrapper

Python package that helps you easily retrieve complete web articles.

[![License: MIT](https://img.shields.io/github/license/erikqu/NewsDataScraper)](https://opensource.org/licenses/MIT)
[![pypi: newsdatascraper](https://img.shields.io/pypi/pyversions/newsdatascraper)](https://pypi.org/project/newsdatascraper/)

## Requirements
- Python 3.5+
- [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- API Key from [NewsApi](https://newsapi.org) or API Key from [GNews](https://gnews.io)

## Installation
```bash
pip3 install newsdatascraper
```

## Usage
```python
from newsdatascraper import Scraper
#To first get a single article on a topic
new_scraper = Scraper('mock-api-key')
articles = new_scraper.fetch_all_articles(query='two sigma', pageSize = 10)

"""
We support two APIs: NewsApi and GNewsApi
To control the API being used change the argument of mode to either 'NEWSPAPER' or 'GNEWS'
"""

new_scraper = Scraper('mock-api-key', mode = 'GNEWS')
articles = new_scraper.fetch_all_articles(query='two sigma', pageSize = 10, 
              dateFrom = "2019-08-04", dateTo = "2019-08-10")

#To access individual articles and their properties
first_article = articles.articles[0]
print(first_article.content)
#We also provide helper functions to serialize the data
articles.toCsv('test.csv')
articles.toPickle('test.pickle')
articles.toJson()
```

## Important Note

Please look at rate limits in the APIs to determine your prefered usage

### Working on the Project
Run format
```bash
black .
```
Run Linter
```bash
pylama -o setup.cfg .
```
Run tests
```bash
pytest
```
Run tests + code coverage
```bash
sh ./scripts/generate_coverage.sh
```
