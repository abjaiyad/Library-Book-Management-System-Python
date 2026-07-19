library_books = {}

while True:

    print("===== LIBRARY BOOK MANAGEMENT =====")
    print("1. Add a book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Show all books")
    print("5. Exit")

    choice = input("Enter Choice (1 to 5): ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        if name in library_books:
            print("Book is already added.")
        else:
            library_books[name] = author
            print("Book added successfully.")
    
    elif choice == "2":
        name = input("Enter book name to search: ")
        if name in library_books:
            print(f"Book name: {name}, Author name: {library_books[name]}")
        else:
            print("Book not found.")

    elif choice == "3":
        name = input("Enter book name to remove: ")
        if name in library_books:
            del library_books[name]
            print("Book removed.")
        else:
            print("Book not found.")
    
    elif choice == "4":
        if len(library_books) == 0:
            print("Library books are empty.")
        else:
            print("\nAll books:")
            for name, author in library_books.items():
                print(name, ":", author)
    
    elif choice == "5":
        print("Thank You.")
        break
    else:
        print("Invalid choice.")