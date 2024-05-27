class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or (len(name) < 2 or len(name) > 16):
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive.")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or (len(value) < 2 or len(value) > 16):
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = value

    def articles(self):
        pass

    def contributors(self):
        pass