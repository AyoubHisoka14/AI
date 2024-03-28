
import exercise
import  calculator
from library import Library
from book import Book
from customer import Customer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




if __name__ == '__main__':

    book1 = Book("Harry Potter", "J. K. Rowling", 1)
    book2 = Book("Game of Thrones", "George R. R. Martin", 2)
    book3 = Book("Lord of The Rings", "J. R. R. Tolkien", 3)

    # Create instances of customers
    customer1 = Customer("Ayoub", 22)
    customer2 = Customer("Amine", 30)

    # Create an instance of the library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register customers with the library
    library.register_customer(customer1)
    library.register_customer(customer2)

    # Display available books
    library.display_available_books()

    # Customers borrow and return books
    customer1.borrow_books([book1, book2])
    customer2.borrow_books([book2, book3])

    customer1.return_books([book1, book2])
    customer2.return_books([book3])

    # Display available books again
    library.display_available_books()

