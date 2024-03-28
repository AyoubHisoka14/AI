import book
import customer

class Library:
    def __init__(self):
        self.books = []
        self.customers = []

    def add_book(self, book):
        self.books.append(book)

    def register_customer(self, customer):
        self.customers.append(customer)

    def display_available_books(self):
        available_books = [book for book in self.books if book.status == "available"]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) is available.")
        else:
            print("No books are available in the library.")