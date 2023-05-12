import csv

class Library:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    def __str__(self):
        return f'Library {self.name} located at {self.location}'

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Member {self.name} with ID {self.id}'

class Item:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return f'Item {self.title} with ID {self.id}'

class Book(Item):
    def __init__(self, id, title):
        super().__init__(id, title)

    def __str__(self):
        return f'Book {self.title} with ID {self.id}'

class Article(Item):
    def __init__(self, id, title):
        super().__init__(id, title)

    def __str__(self):
        return f'Article {self.title} with ID {self.id}'

class DigitalMedia(Item):
    def __init__(self, id, title):
        super().__init__(id, title)

    def __str__(self):
        return f'Digital Media {self.title} with ID {self.id}'

class Borrowing:
    def __init__(self, transaction_id, member_id, item_id, date_borrowed, date_returned=None):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.item_id = item_id
        self.date_borrowed = date_borrowed
        self.date_returned = date_returned

    def __str__(self):
        return f'Transaction {self.transaction_id}: Member {self.member_id} borrowed item {self.item_id} on {self.date_borrowed}. Returned on {self.date_returned if self.date_returned else "not returned yet"}'

def load_data():
    library = []
    items = []
    members = []
    borrowings = []

    with open('library.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            library.append(Library(*row))

    with open('items.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            id, type, title = row
            if type == 'Book':
                items.append(Book(id, title))
            elif type == 'Article':
                items.append(Article(id,                title))
            elif type == 'DigitalMedia':
                items.append(DigitalMedia(id, title))

    with open('members.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            members.append(Member(*row))

    with open('borrowing.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            borrowings.append(Borrowing(*row))

    return library, items, members, borrowings

def save_data(library, items, members, borrowings):
    with open('library.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        for lib in library:
            writer.writerow([lib.id, lib.name, lib.location])

    with open('items.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in items:
            writer.writerow([item.id, item.__class__.__name__, item.title])

    with open('members.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        for member in members:
            writer.writerow([member.id, member.name])

    with open('borrowing.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        for borrowing in borrowings:
            writer.writerow([borrowing.transaction_id, borrowing.member_id, borrowing.item_id, borrowing.date_borrowed, borrowing.date_returned])

def handle_input(library, items, members, borrowings):
    while True:
        print("\n1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. Add Member")
        print("5. Edit Member")
        print("6. Delete Member")
        print("7. Borrow Item")
        print("8. Return Item")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(items)
        elif choice == '2':
            edit_item(items)
        elif choice == '3':
            delete_item(items)
        elif choice == '4':
            add_member(members)
        elif choice == '5':
            edit_member(members)
        elif choice == '6':
            delete_member(members)
        elif choice == '7':
            borrow_item(members, items, borrowings)
        elif choice == '8':
            return_item(borrowings)
        elif choice == '9':
            save_data(library, items, members, borrowings)
            break
        else:
            print("Invalid choice, please try again.")

# Define the functions to add, edit, delete, borrow, return...
def add_item(items):
    id = input("Enter item ID: ")
    title = input("Enter item title: ")
    type = input("Enter item type (Book, Article, DigitalMedia): ")
    if type == 'Book':
        items.append(Book(id, title))
    elif type == 'Article':
        items.append(Article(id, title))
    elif type == 'DigitalMedia':
        items.append(DigitalMedia(id, title))
    else:
        print("Invalid type, please try again.")

def edit_item(items):
    id = input("Enter the ID of the item you want to edit: ")
    for item in items:
        if item.id == id:
            new_title = input("Enter the new title for this item: ")
            item.title = new_title
            print("Item updated successfully.")
            return
    print("Item not found.")

def delete_item(items):
    id = input("Enter the ID of the item you want to delete: ")
    for i, item in enumerate(items):
        if item.id == id:
            del items[i]
            print("Item deleted successfully.")
            return
    print("Item not found.")

def add_member(members):
    id = input("Enter new member ID: ")
    name = input("Enter member name: ")
    members.append(Member(id, name))

def edit_member(members):
    id = input("Enter the ID of the member you want to edit: ")
    for member in members:
        if member.id == id:
            new_name = input("Enter the new name for this member: ")
            member.name = new_name
            print("Member updated successfully.")
            return
    print("Member not found.")

def delete_member(members):
    id = input("Enter the ID of the member you want to delete: ")
    for i, member in enumerate(members):
        if member.id == id:
            del members[i]
            print("Member deleted successfully.")
            return
    print("Member not found.")

def borrow_item(members, items, borrowings):
    member_id = input("Enter your member ID: ")
    item_id = input("Enter the ID of the item you want to borrow: ")
    for member in members:
        if member.id == member_id:
            for item in items:
                if item.id == item_id:
                    date_borrowed = input("Enter the date borrowed (in YYYY-MM-DD format): ")
                    borrowings.append(Borrowing(len(borrowings) + 1, member_id, item_id, date_borrowed))
                    print("Item borrowed successfully.")
                    return
            print("Item not found.")
            return
    print("Member not found.")

def return_item(borrowings):
    transaction_id = input("Enter the transaction ID of the item you want to return: ")
    for borrowing in borrowings:
        if borrowing.transaction_id == transaction_id:
            date_returned = input("Enter the date returned (in YYYY-MM-DD format): ")
            borrowing.date_returned = date_returned
            print("Item returned successfully.")
            return
    print("Transaction not found.")


if __name__ == "__main__":
    library, items, members, borrowings = load_data()
    handle_input(library, items, members, borrowings)



