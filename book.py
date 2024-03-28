class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "available"  # By default, a book is available

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            return True
        else:
            return False

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            return True
        else:
            return False