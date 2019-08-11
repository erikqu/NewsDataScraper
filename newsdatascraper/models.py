from datetime import date
import json
import csv
import pickle


class ArticleFromJson:
    '''Data model for one article'''

    def __init__(self, author: str, title: str, description: str, url: str, datePublished, content: str):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.datePublished = datePublished
        self.content = content


class Articles:
    '''Model to contain a list of article data. Also has functions to serialize that data'''

    def __init__(self, articles: list):
        self.articles = articles

    def toCsv(self, csv_name: str):
        '''Create a .csv file from the articles data to better visualize'''
        with open(csv_name, 'w') as f:
            writer = csv.DictWriter(f, vars(self.articles[0]).keys())
            writer.writeheader()
            for article in self.articles:
                writer.writerow(vars(article))
        f.close()

    def toJson(self):
        '''Serializes the article objects to json'''
        article_list = [vars(article) for article in self.articles]
        return json.dumps({'articles': article_list})

    def pickle(self, pickle_name: str):
        '''Serialization of article objects to byte stream'''
        with open(pickle_name, 'wb') as f:
            pickle.dump(self.articles, f)
            f.close()
