class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        magazine._articles.append(self)
        author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or 5 <= len(value) <= 50:
            raise Exception("The title must be a string with characters between 5 and 50")
        self._title = value
        
    @property
    def authors(self):
        return self._author
    
    @authors.setter
    def authors(self, value):
        if not isinstance(value, Author):
            raise Exception("The author must be an instance of class Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("The magazine must be an instance of class Magazine")
        self._magazine = value
        
    
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) and len(name) < 0:
            raise Exception("The author name should be a string with character length greater than 0")
        self._name = name
        
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))


    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass