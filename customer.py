import book


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_books = []

    def borrow_books(self, books:list):
        for book in books:
            if book.borrow():
                self.borrowed_books.append(book)
            else:
                print(f"{book.title} is not available for borrowing.")

    def return_books(self, books:list):
        for book in books:
            if book in self.borrowed_books:
                book.return_book()
                self.borrowed_books.remove(book)
            else:
                print(f"{book.title} was not borrowed by {self.name}.")