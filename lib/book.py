# lib/book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
