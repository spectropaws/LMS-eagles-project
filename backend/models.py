class Book:
    def __init__(self, book_id, book_name, issuer_name=None):
        self._book_id = book_id
        self._book_name = book_name
        self._issuer_name = issuer_name

    def get_book_id(self):
        return self._book_id

    def get_book_name(self):
        return self._book_name

    def get_issuer_name(self):
        return self._issuer_name

    def set_book_id(self, book_id):
        self._book_id = book_id

    def set_book_name(self, book_name):
        self._book_name = book_name

    def set_issuer_name(self, issuer_name):
        self._issuer_name = issuer_name


class Member:
    def __init__(self, member_id, member_name):
        self._member_id = member_id
        self._member_name = member_name
        self._issued_books = []

    def get_member_id(self):
        return self._member_id

    def get_member_name(self):
        return self._member_name

    def get_issued_books(self):
        return self._issued_books

    def set_member_id(self, member_id):
        self._member_id = member_id

    def set_member_name(self, member_name):
        self._member_name = member_name

    def set_issued_books(self, issued_books):
        self._issued_books = issued_books

    def issue_book(self, book):
        self._issued_books.append(book)

    def return_book(self, book):
        self._issued_books.remove(book)


