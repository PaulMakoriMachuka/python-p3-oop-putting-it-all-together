#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0, author=None):
        self.title = title
        self.page_count = page_count
        self.author = author

    # title
    def get_title(self):
        return self._title

    def set_title(self, value):
        if not isinstance(value, str):
            print("title must be a string")
        else:
            self._title = value

    title = property(get_title, set_title)

    # author
    def get_author(self):
        return getattr(self, "_author", None)

    def set_author(self, value):
        if value is not None and not isinstance(value, str):
            print("author must be a string")
        else:
            self._author = value

    author = property(get_author, set_author)

    # page_count
    def get_page_count(self):
        return getattr(self, "_page_count", 0)

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    page_count = property(get_page_count, set_page_count)

    # behavior
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
