
from author import Author


def isbn_is_valid(isbn):
    pass


class Book:
    __books = []

    def __init__(self, title: str) -> None:
        self.title = title
        self.__isbn = ''
        self.__author = []
        self.__books.append(self)

    @classmethod
    def books(cls):
        return cls.__books

    def __str__(self) -> str:
        return f'{self.title}'

    @property
    def authors(self) -> list:
        return [author.full_name for author in self.__author if len(self.__author) > 0]
    
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        if isbn_is_valid(isbn):
            self.__isbn = isbn

    def add_author(self, author: Author) -> None:
        if isinstance(author, Author) and author not in self.__author:
            self.__author.append(author)
