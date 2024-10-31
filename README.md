# Address Book CLI Application

A command-line address book application built in Python using object-oriented programming principles. The project features a clean, modular architecture with proper package structure and data validation.

## Project Structure

```
address_book/
├── models/
│   ├── __init__.py     # Package initialization and exports
│   ├── field.py        # Base field class
│   ├── name.py         # Name field implementation
│   ├── phone.py        # Phone field implementation
│   ├── record.py       # Contact record class
│   └── address_book.py # Main address book container
└── main.py             # Application entry point
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/address-book.git
cd address-book
```

2. Ensure you have Python 3.6 or higher installed:
```bash
python --version
```

## Class Structure

### Models Package (`models/`)

#### Field (`field.py`)
Base class for all field types:
```python
from models import Field

field = Field("some value")
print(field)  # Outputs: some value
```

#### Name (`name.py`)
Handles contact names with validation:
```python
from models import Name

name = Name("John Doe")  # Valid
name = Name("")  # Raises ValueError: Name cannot be empty
```

#### Phone (`phone.py`)
Manages phone numbers with validation:
```python
from models import Phone

phone = Phone("1234567890")  # Valid
phone = Phone("123")  # Raises ValueError: Phone must be 10 digits long
phone = Phone("abcd")  # Raises ValueError: Phone must contain only digits
```

#### Record (`record.py`)
Manages individual contacts:
```python
from models import Record

record = Record("John Doe")
record.add_phone("1234567890")
record.add_phone("9876543210")
record.remove_phone("1234567890")
record.edit_phone("9876543210", "1112223333")
```

#### AddressBook (`address_book.py`)
Main container for all contacts:
```python
from models import AddressBook, Record

book = AddressBook()
record = Record("John Doe")
book.add_record(record)
found = book.find("John Doe")
book.delete("John Doe")
```

## Usage Examples

### Basic Usage
```python
from models import AddressBook, Record

# Create new address book
book = AddressBook()

# Add new contact
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")
book.add_record(john)

# Find and edit contact
contact = book.find("John")
if contact:
    contact.edit_phone("1234567890", "1112223333")
    print(contact)  # Displays: Contact name: John, phones: 1112223333; 5555555555
```

### Error Handling
The application handles various error cases:
```python
# Invalid phone number
try:
    record.add_phone("123")  # Raises ValueError
except ValueError as e:
    print(e)  # Phone must be 10 digits long

# Non-existent contact
try:
    book.delete("Jane")  # Raises KeyError
except KeyError:
    print("Contact not found")
```

## Validation Rules

### Name Validation
- Cannot be empty string
- Must be provided when creating a contact

### Phone Validation
- Must be exactly 10 digits
- Can only contain numeric characters
- Must be provided as string
- No duplicate phones per contact

## Development

### Project Organization
- Models are organized in the `models` package
- Each class has its own module
- Clean imports through `__init__.py`

### Import Structure
```python
# Recommended import style
from models import AddressBook, Record, Name, Phone

# Instead of
from models.address_book import AddressBook
from models.record import Record
# etc...
```

## Future Improvements

1. Data Persistence
   - Add save/load functionality
   - Support multiple storage backends (JSON, SQLite)

2. Additional Fields
   - Email addresses
   - Physical addresses
   - Birth dates
   - Notes

3. Enhanced Functionality
   - Search by phone number
   - Partial name matching
   - Contact groups/categories
   - Import/export (CSV, vCard)

4. User Interface
   - Add command history
   - Interactive mode improvements
   - Better error messages
   - Help system

## Dependencies
- Python 3.6+
- No external packages required

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
