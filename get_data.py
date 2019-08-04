
from newspaper import Article 
import requests


CURKEY = "fa8ad475cba8446fa8a0ee7018d79c50"


def fetch_all_articles(query): 
    global CURKEY
    url = "https://newsapi.org/v2/everything?q="+ query +"&apiKey=" + CURKEY
    results = requests.get(url).json() 
    all_articles = results["articles"] 



def get_text(url): 
    article = Article(url) 
    article.download() 
    article.parse() 
    return article.text
