from __future__ import annotations

from typing import List
from typing import Optional

from models import Name
from models import Phone


class Record:
    """Class representing a contact record.

    Stores and manages a contact's name and phone numbers.

    Attributes:
        name (Name): The contact's name.
        phones (List[Phone]): List of the contact's phone numbers.
    """

    def __init__(self, name: str) -> None:
        """Initialize a new contact record.

        Args:
            name: The contact's name.
        """
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone_number: str) -> None:
        """Add a new phone number to the contact.

        Args:
            phone_number: The phone number to add.

        Raises:
            ValueError: If the phone number already exists for this contact.
        """
        phone = Phone(phone_number)
        if self.find_phone(phone_number):
            raise ValueError("Phone number already exists")
        self.phones.append(phone)

    def remove_phone(self, phone_number: str) -> None:
        """Remove a phone number from the contact.

        Args:
            phone_number: The phone number to remove.

        Raises:
            ValueError: If the phone number is not found.
        """
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number.

        Args:
            old_phone: The phone number to replace.
            new_phone: The new phone number.

        Raises:
            ValueError: If the old phone number is not found.
        """
        phone = self.find_phone(old_phone)
        if not phone:
            raise ValueError("Phone number not found")
        phone.value = new_phone

    def find_phone(self, phone_number: str) -> Phone | None:
        """Find a phone number in the contact's phones.

        Args:
            phone_number: The phone number to search for.

        Returns:
            Optional[Phone]: The found Phone object or None if not found.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self) -> str:
        """Return string representation of the contact.

        Returns:
            str: Formatted string with contact's name and phone numbers.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
