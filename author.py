
class Author:
    authors = []

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.authors.append(self)

    @classmethod
    def authors_list(cls):
        return cls.authors

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name
