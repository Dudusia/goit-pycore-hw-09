from __future__ import annotations

from models import Field


class Name(Field):
    """Class representing a contact's name.

    Extends the Field class with specific validation for name values.
    Names cannot be empty strings.

    Attributes:
        _value (str): Protected storage for the name value.
    """

    def __init__(self, value: str) -> None:
        """Initialize a new name field.

        Args:
            value: The name string to store.

        Raises:
            ValueError: If the name is an empty string.
        """
        self._value = None
        self.value = value

    @property
    def value(self) -> str:
        """Get the stored name value.

        Returns:
            str: The stored name.
        """
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        """Set the name value with validation.

        Args:
            new_value: The new name to store.

        Raises:
            ValueError: If the new name is an empty string.
        """
        if not new_value:
            raise ValueError("Name cannot be empty")
        self._value = new_value
