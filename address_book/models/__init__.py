"""Address Book package.

This package provides classes for managing an address book with contacts
and their phone numbers.

Classes:
    Field: Base class for all fields.
    Name: Class for storing and validating contact names.
    Phone: Class for storing and validating phone numbers.
    Record: Class for managing individual contacts.
    AddressBook: Main class for storing and managing all contacts.
"""
from __future__ import annotations

from .address_book import AddressBook
from .field import Field
from .name import Name
from .phone import Phone
from .record import Record

__all__ = ["Field", "Name", "Phone", "Record", "AddressBook"]
