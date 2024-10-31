from __future__ import annotations

from models import AddressBook
from models import Record


def main():
    # Create a new address book
    book = AddressBook()

    # Create and add John's record
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Create and add Jane's record
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all records
    for name, record in book.data.items():
        print(record)

    # Find and edit John's phone
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        # Find specific phone
        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")

    # Delete Jane's record
    book.delete("Jane")


if __name__ == "__main__":
    main()
