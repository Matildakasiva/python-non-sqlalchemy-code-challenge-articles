
class Article:
    all = []
    
    # all - is an empty list, stores instances of Article

    def __init__(self, author: 'Author', magazine: 'Magazine', title: str):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        self._author = author

        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = magazine

        if not isinstance(title, str) or 5 > len(title) or len(title) > 50:
            raise Exception("The title must be a string with characters between 5 and 50")
        self.title = title
        
        Article.all.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, magazine_name):
        if not isinstance(magazine_name, str):
            raise Exception("Title must be a string")
        if len(magazine_name) < 5 or len(magazine_name) > 50:
            raise Exception("Title must be a string between 5 and 50 characters long")
        self._title = magazine_name

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, magazine_name):
        if not isinstance(magazine_name, Author):
            raise Exception("Author must be an instance of Author")
        self._author = magazine_name

    @property
    def magazine(self):
        return self._magazine  

    @magazine.setter
    def magazine(self, magazine_name):
        if not isinstance(magazine_name, Magazine):
            raise Exception("Magazine must be an instance of Magazine")  
        self._magazine = magazine_name    
   
        
class Author:

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("The author name should be a string")
        if len(name) == 0:
            raise Exception("The author name should have a character length greater than 0")
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, author_name):
        if hasattr(self, '_name'):
            raise Exception("Should not be able to change the author after instantiated.")
        if not isinstance(author_name, str):
            raise Exception("The name should be a type of string")
        if len(author_name) <= 0:
            raise Exception("The name should be longer than 0 characters")
        self._name = author_name

    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    # Article returns a list (written by author)

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))
    
    # magazine returns a list (written by author)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
      if not self.articles():
        return None
      return list(set(magazine.category for magazine in self.magazines()))
    
    # returns a list of all magazine categories written by author if 0 returns None
    
class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("The magazine name should be a string")
        if len(name) < 2 or len(name) > 16:
            raise Exception("The magazine name should have characters between 2 and 16, inclusive")
        self._name = name

        if not isinstance(category, str):
            raise Exception("The magazine category should be a string")
        if len(category) == 0:
            raise Exception("The magazine category should have characters longer than 0, inclusive")
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("The magazine name should be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("The magazine name should have characters between 2 and 16, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("The magazine category should be a string")
        if len(new_category) == 0:
            raise Exception("The magazine category should have characters longer than 0, inclusive")
        self._category = new_category

    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles ))
    # returns a list of authors who have written in the magazine
        
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    # returns a list of articles published in magazine

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        if not contributing_authors:
            return None
        return contributing_authors
    # returns a list of authors who have written more than two magazine articles
    
    