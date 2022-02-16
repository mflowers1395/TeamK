import sys

def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print("Title: " + title)
        print("Author: " + book ["author"])
        print("Publication Year: " + book ["pubyear"])
    else:
        print("Sorry, " + title + " wasn't found. Please try a different search.")
def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode =="add" and title in book_catalog:
        print(title + "Sorry, this book already exists in the catalog.")
        response = input ("Would you like to edit it? (Y/N): ")
        if(reponse != "y" or "Y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(title + " doesn;t exist in the catalog.")
        reponse = input("Would you like to add this book into the catalog? (Y/N): ")
        if (response != "y" or "Y"):
            return

    author = input("Author name: ")
    pubyear = input("Publication year: ")

    book = {"author": author,
            "pubyear": pubyear}

    book_catalog[title] = book

def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + "removed from the catalog.")
    else:
        print(title + "doesn't exist in the catalog.")

def display_menu():
    print("The Book Catalog")
    print()
    print("Command Menu")
    print("show - Show book info")
    print("add - Add book")
    print("edit - Edit book")
    print("del - Delete book")
    print("exit- Exit program")

def main():
    display_menu()
    book_catalog = {
        "The Hobbit":
        {"author": "J. R. R.R Tolkien",
        "pubyear" : "1937"}
        }
    while True:
        print()
        command = input("Command: ")
        if command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog,mode="add")
        elif command == "edit":
            add_edit_book(book_catalog,mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Catalog Closed")
            break
