import json
import csv
import pickle


class ArticleFromJson:  # pragma: no cover
    """Data model for one article"""

    def __init__(
        self,
        author: str,
        publisher: str,
        title: str,
        description: str,
        url: str,
        datePublished,
        content: str,
    ):
        self.author = author
        self.publisher = publisher
        self.title = title
        self.description = description
        self.url = url
        self.datePublished = datePublished
        self.content = content

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__dict__ == other.__dict__


class Articles:  # pragma: no cover
    """Model to contain a list of article data.
    Also has functions to serialize that data"""

    def __init__(self, articles: list):
        self.articles = articles

    def __add__(self, other: 'Articles'):
        articles = self.articles + other.articles
        return Articles(articles)

    def __radd__(self, other: 'Articles'):
        articles = self.articles + other.articles
        return Articles(articles)

    def to_csv(self, csv_name: str):
        """Create a .csv file from the articles data to better visualize"""
        with open(csv_name, "w") as f:
            writer = csv.DictWriter(f, vars(self.articles[0]).keys())
            writer.writeheader()
            for article in self.articles:
                writer.writerow(vars(article))
        f.close()

    def to_json(self):
        """Serializes the article objects to json"""
        article_list = [vars(article) for article in self.articles]
        return json.dumps({"articles": article_list})

    def to_pickle(self, pickle_name: str):
        """Serialization of article objects to byte stream"""
        with open(pickle_name, "wb") as f:
            pickle.dump(self.articles, f)
            f.close()

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        for index, article in enumerate(self.articles):
            if article != other.articles[index]:
                return False
        return True
