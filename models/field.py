from __future__ import annotations


class Field:
    """Base class for all fields in the address book.

    This class serves as a parent class for specific field types like Name and Phone,
    providing basic functionality for value storage and string representation.

    Attributes:
        value: The value stored in the field.
    """

    def __init__(self, value: str) -> None:
        """Initialize a new field with a value.

        Args:
            value: Initial value for the field.
        """
        self.value = value

    def __str__(self) -> str:
        """Return string representation of the field value.

        Returns:
            str: String representation of the stored value.
        """
        return str(self.value)
