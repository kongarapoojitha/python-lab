
# Library Management System Using OOP

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({
            "name": book,
            "available": True
        })
        print("Book added successfully!")

    def display_books(self):
        print("\n===== AVAILABLE BOOKS =====")

        if not self.books:
            print("No books in library.")
            return

        for book in self.books:
            status = "Available" if book["available"] else "Borrowed"
            print(book["name"], "-", status)

    def borrow_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed!")
                return

        print("Book not found!")

    def return_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        name = input("Enter book name to borrow: ")
        library.borrow_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "5":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Try again.")
