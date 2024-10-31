from __future__ import annotations

from models import Field


class Phone(Field):
    """Class representing a phone number.

    Extends the Field class with specific validation for phone numbers.
    Phone numbers must be exactly 10 digits.

    Attributes:
        _value (str): Protected storage for the phone number.
    """

    def __init__(self, value: str) -> None:
        """Initialize a new phone field.

        Args:
            value: The phone number string to store.

        Raises:
            ValueError: If the phone number is invalid.
        """
        self._value: str = ""
        self.value = value

    @property
    def value(self) -> str:
        """Get the stored phone number.

        Returns:
            str: The stored phone number.
        """
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        """Set the phone number with validation.

        Args:
            new_value: The new phone number to store.

        Raises:
            ValueError: If the phone number is not exactly 10 digits or contains
                non-digit characters.
        """
        if not isinstance(new_value, str):
            raise ValueError("Phone must be a string")
        if not new_value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(new_value) != 10:
            raise ValueError("Phone must be 10 digits long")
        self._value = new_value
