from mock import Mock


class Category:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        Category.query = Mock()
        Category.query.filter_by = Mock(return_value=DBQuerySet())

    def to_dict(self):
        return self.__dict__


class DBQuerySet(set):
    def __init__(self):
        super(DBQuerySet, self).__init__()
        self.delete = Mock()


class Session:
    def __init__(self):
        self.add = Mock()
        self.commit = Mock()
        self.query = Mock()


class DB:
    def __init__(self):
        self.session = Session()
