class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title

    @property
    def title(self):
        if not isinstance(self._title, str) or (len(self._title) < 5 or len(self._title) > 50):
            raise ValueError("The title must be a string with characters between 5 and 50")
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed after the article is instantiated")
        if not isinstance(value, str) or (len(value) < 5 or len(value) > 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def __setattr__(self, name, value):
        if name == "title" and hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed after the article is instantiated")
        super().__setattr__(name, value)