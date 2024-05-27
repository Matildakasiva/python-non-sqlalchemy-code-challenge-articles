
class author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a type of str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self, name):
        return self._name
     
    def articles(self):
        pass

    def magazines(self):
        pass
          