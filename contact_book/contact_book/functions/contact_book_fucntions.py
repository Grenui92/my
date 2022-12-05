from contact_book.contact_book.classes.class_contact_book import AddressBook
from contact_book.contact_book.classes.decorators import bug_catcher

"""CONTACTBOOK"""


@bug_catcher
def main():
    book = AddressBook()
    try:
        print(book.load_from_file())
    except FileNotFoundError:
        print(book.save_to_file())
    return book


@bug_catcher
def create_contact(name: str, book: AddressBook) -> str:
    return book.create_new_contact(name)


@bug_catcher
def add_phone_to_contact(name: str, phone: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.add_phone(phone)


@bug_catcher
def add_email_to_contact(name: str, email: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.add_email(email)


@bug_catcher
def add_address_to_contact(name: str, address: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.add_address(address)


@bug_catcher
def set_birthday(name: str, date_birthday: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.set_birthday(date_birthday)


@bug_catcher
def edit_contact_information(name: str, field: str, old: str, new: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.edit_contact_information(field, old, new)


@bug_catcher
def edit_name(old_name: str, new_name: str, book: AddressBook) -> str:
    return book.edit_contact(old_name, new_name)


@bug_catcher
def search_contact(name: str, book: AddressBook) -> str:
    return book.search_contact(name)


@bug_catcher
def search_in_all_information(information: str, book: AddressBook) -> list:
    return book.search_in_all_contact_information(information)


@bug_catcher
def show_nearest_birthdays(days: str, book: AddressBook) -> list:
    """Here we call information about birthdays which will happen within the next DAYS days.
    If DAYS argument is empty - default DAYS in show_upcoming_birthday() == 7"""

    if days:
        n = int(days)  # Check isinstance(days, int) and also our class method waiting for type(int)
        return book.show_upcoming_birthdays(n=n)
    else:
        return book.show_upcoming_birthdays()


@bug_catcher
def days_to_birthday(name: str, book: AddressBook) -> str:
    record = book[name]  # Check if this record exists
    return record.days_to_birthday()


@bug_catcher
def days_to_birthday_for_all(book: AddressBook) -> list:
    return book.days_to_birthdays_all_contacts()


@bug_catcher
def show_contacts(book: AddressBook) -> list:
    return book.show_all_contacts()


@bug_catcher
def clear_contact(name: str, book: AddressBook, field: str):
    return book.clear_contact(name=name, field=field)


@bug_catcher
def clear_book(answer: str, book: AddressBook) -> str:
    if answer.upper() == "Y":
        return book.clear_all_book()
    else:
        return "Operation 'delete all contacts' canceled."


@bug_catcher
def save_to_file(book: AddressBook):
    return book.save_to_file()


"""END CONTACTBOOK"""
if __name__ == "__main__":
    main()
