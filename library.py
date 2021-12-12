from itertools import chain

from book import Book


class LibraryBook(Book):
    lib_books = []

    def __init__(self, title: str, index: int) -> None:
        super().__init__(title)
        self.index = index
        self.__borrowed = False
        self.lib_books.append(self)

    def __str__(self):
        return f'{self.index} - {self.title}'

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        self.__borrowed = borrowed


class Library:
    class BookNotInBooksErr(Exception):
        pass

    class BookNotAvailableErr(Exception):
        pass

    def __init__(self, name: str) -> None:
        self.name = name
        self.__books = []
        # self.__books_count = 0
        self.__books_borrowed = 0

    def __str__(self) -> str:
        return f'Biblioteka {self.name} - zawiera {self.books_count} książkę/książek'

    @property
    def books_count(self) -> int:
        return len(self.__books)

    @property
    def books(self) -> list:
        return self.__books

    def add_book(self, book: LibraryBook) -> None:
        if not isinstance(book, LibraryBook):
            raise ValueError("Invalid book type")

        self.__books.append(book)

    def del_book(self, book: LibraryBook) -> None:
        """

        :param book:
        :return:
        """
        if not isinstance(book, LibraryBook):
            raise ValueError("Invalid book type")
        try:
            if book not in self.__books:
                raise self.BookNotInBooksErr

            self.__books.remove(self.__books.index(book))
        except self.BookNotInBooksErr:
            print('This book is not on a list')

    @property
    def titles(self) -> set:
        return set(
            [book.title for book in self.books]
        )

    @property
    def authors(self) -> set:
        return set(
            list(
                chain(*[book.authors for book in self.books if len(book.authors) > 0])
            )
        )

    def borrow(self, book: LibraryBook):
        """

        :param book:
        :return:
        """
        try:
            if book not in self.books:
                raise self.BookNotInBooksErr

            if book.borrowed:
                raise self.BookNotAvailableErr

            book.borrowed = True
        except self.BookNotInBooksErr:
            print('This book is not on a list')
        except self.BookNotAvailableErr:
            print('This book is not available!')

    def give_back_book(self, book: LibraryBook):
        pass

    @property
    def books_borrowed(self) -> list:
        """

        :return: list of book objects
        """
        return [book for book in self.books if book.borrowed]

    @property
    def books_available(self) -> list:
        """

        :return: list of book objects
        """
        return [book for book in self.books if not book.borrowed]
