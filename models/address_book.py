from __future__ import annotations

from collections import UserDict
from typing import Optional

from models import Record


class AddressBook(UserDict):
    """Class representing an address book.

    Inherits from UserDict to provide dictionary-like behavior for storing
    and managing contact records.

    Attributes:
        data (dict): Internal storage for contact records.
    """

    def add_record(self, record: Record) -> None:
        """Add a new record to the address book.

        Args:
            record: The Record object to add.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name.

        Args:
            name: The name to search for.

        Returns:
            Optional[Record]: The found Record object or None if not found.
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by name.

        Args:
            name: The name of the record to delete.

        Raises:
            KeyError: If the record is not found.
        """
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Record not found")
