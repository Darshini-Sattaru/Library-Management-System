books = []


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    book = {"title": title, "author": author, "status": "Available"}
    books.append(book)
    print(f"'{title}' added to the library!\n")


def view_books():
    if len(books) == 0:
        print("No books in the library yet.\n")
        return

    print("\n--- Library Books ---")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} by {book['author']} - {book['status']}")
    print()


def search_book():
    keyword = input("Enter title or author to search: ").strip().lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]

    print()
    if not results:
        print("No matching books found.\n")
        return

    print("--- Search Results ---")
    for book in results:
        print(f"{book['title']} by {book['author']} - {book['status']}")
    print()


def get_valid_index():
    view_books()
    if len(books) == 0:
        return None
    try:
        choice = int(input("Enter book number: ")) - 1
        if choice < 0 or choice >= len(books):
            print("Invalid book number.\n")
            return None
        return choice
    except ValueError:
        print("Please enter a valid number.\n")
        return None


def issue_book():
    index = get_valid_index()
    if index is None:
        return

    if books[index]["status"] == "Issued":
        print("This book is already issued.\n")
    else:
        books[index]["status"] = "Issued"
        print(f"'{books[index]['title']}' issued successfully!\n")


def return_book():
    index = get_valid_index()
    if index is None:
        return

    if books[index]["status"] == "Available":
        print("This book was not issued.\n")
    else:
        books[index]["status"] = "Available"
        print(f"'{books[index]['title']}' returned successfully!\n")


def delete_book():
    index = get_valid_index()
    if index is None:
        return

    removed = books.pop(index)
    print(f"Deleted: {removed['title']}\n")


def show_menu():
    print("========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.\n")


if __name__ == "__main__":
    main()
