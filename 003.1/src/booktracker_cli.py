import json
import os

# Define the file to store book data
DATA_FILE = 'books.json'

def load_books():
    """Loads books from the JSON data file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupted JSON file
                return []
    return []

def save_books(books):
    """Saves books to the JSON data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book(books):
    """Adds a new book to the tracker."""
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    year = input("Enter publication year (optional): ").strip()

    if not title or not author:
        print("Title and author cannot be empty. Book not added.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year if year else "N/A",
        "read": False
    }
    books.append(book)
    save_books(books)
    print(f"Book '{title}' by {author} added successfully!")

def list_books(books):
    """Lists all books in the tracker."""
    if not books:
        print("No books in your tracker yet. Add some!")
        return

    print("\n--- Your Books ---")
    for i, book in enumerate(books):
        status = "Read" if book["read"] else "Unread"
        print(f"{i + 1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {status}")
    print("------------------")

def mark_as_read(books):
    """Marks a book as read."""
    list_books(books)
    if not books:
        return

    try:
        book_index = int(input("Enter the number of the book to mark as read: ")) - 1
        if 0 <= book_index < len(books):
            if not books[book_index]["read"]:
                books[book_index]["read"] = True
                save_books(books)
                print(f"Book '{books[book_index]['title']}' marked as read.")
            else:
                print(f"Book '{books[book_index]['title']}' is already marked as read.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_book(books):
    """Deletes a book from the tracker."""
    list_books(books)
    if not books:
        return

    try:
        book_index = int(input("Enter the number of the book to delete: ")) - 1
        if 0 <= book_index < len(books):
            deleted_book = books.pop(book_index)
            save_books(books)
            print(f"Book '{deleted_book['title']}' by {deleted_book['author']} deleted.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_menu():
    """Displays the main menu options."""
    print("\n--- Book Tracker Menu ---")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Mark a book as read")
    print("4. Delete a book")
    print("5. Exit")
    print("-------------------------")

def main():
    """Main function to run the book tracker application."""
    books = load_books()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            mark_as_read(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            print("Exiting Book Tracker. Happy reading!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
