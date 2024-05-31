
class Article: 
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        self.author = author

        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self.magazine = magazine

        if not isinstance(title, str) or 5 > len(title) or len(title) > 50:
            raise Exception("The title must be a string with characters between 5 and 50")
        self.title = title
        
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise Exception("Title must be a string between 5 and 50 characters long")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine  

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")  
        self._magazine = value    
   
        
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("The author name should be a string with a character length greater than 0")
        self._name = name
        self._articles = []
        self.magazines = set()
        self.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(title, self, magazine)
        self.articles.append(article)
        self.magazines.append(magazine)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for article in self._articles for magazine in [article.magazine]))


class Magazine:
    all = []

    def __init__(self, name: str, category: str):
        if not isinstance(name, str) or (2 > len(name) or len(name) > 16):
            raise Exception("The magazine name should be a string with characters between 2 and 16, inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("The magazine category should be a string with characters longer than 0, inclusive")
        self.name = name
        self.category = category
        self.articles = []
        self.contributors = set()
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or (2 > len(value) or len(value) > 16):
            raise Exception("The magazine name should be a string with characters between 2 and 16, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("The magazine category should be a string with characters longer than 0, inclusive")
        self._category = value

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        authors = set()
        for article in self._articles:
            authors.append(article.author)
        return [author for author in authors if len(authors.articles) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles))
