import os

class Book:
    def __init__(self, isbn, title, author, year, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price

class Bookstore:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass
            print(f"File '{self.filename}' does not exist. A new file has been created.")
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                for line in file:
                    isbn, title, author, year, price = line.strip().split('|')
                    book = Book(isbn, title, author, year, price)
                    self.books.append(book)
        except FileNotFoundError:
            # This should not happen because we create the file if it does not exist
            pass

    def save_books(self):
        with open(self.filename, mode='w', encoding='utf-8') as file:
            for book in self.books:
                file.write(f'{book.isbn}|{book.title}|{book.author}|{book.year}|{book.price}\n')

    def add_book(self, isbn, title, author, year, price):
        new_book = Book(isbn, title, author, year, price)
        self.books.append(new_book)
        self.save_books()

    def view_books(self):
        for book in self.books:
            print(f'ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Price: {book.price}')

    def update_book(self, isbn, title=None, author=None, year=None, price=None):
        for book in self.books:
            if book.isbn == isbn:
                if title: book.title = title
                if author: book.author = author
                if year: book.year = year
                if price: book.price = price
                self.save_books()
                return True
        return False

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return True
        return False

def main():
    filename = input("Enter the filename to store the book data (e.g., 'books.txt'): ")
    bookstore = Bookstore(filename)

    while True:
        print("\nBookstore Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year: ")
            price = input("Enter Price: ")
            bookstore.add_book(isbn, title, author, year, price)
            print("Book added successfully!")
        
        elif choice == '2':
            print("\nList of Books:")
            bookstore.view_books()
        
        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            print("Enter new details (leave blank to keep current value):")
            title = input("Enter new Title: ")
            author = input("Enter new Author: ")
            year = input("Enter new Year: ")
            price = input("Enter new Price: ")
            if bookstore.update_book(isbn, title, author, year, price):
                print("Book updated successfully!")
            else:
                print("Book not found!")
        
        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            if bookstore.delete_book(isbn):
                print("Book deleted successfully!")
            else:
                print("Book not found!")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
