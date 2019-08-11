# NewsDataScrapper
Python package that helps you easily get news data

## Requirements
- Python 3.5+
- [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- Api Key from [NewsApi](https://newsapi.org)

## Usage
```python
from newsdatascraper import Scraper
#To first get the articles
new_scraper = Scraper('mock-api-key')
articles = new_scraper.fetch_all_articles(query='two-sigma')
#To access individual articles and their properties
first_article = articles.articles[0]
print(first_article.content)
#We also provide helper functions to serialize the data
articles.toCsv('test.csv')
articles.pickle('test.pickle')
articles.json()
```