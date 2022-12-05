from contact_book.contact_book.classes.class_contact_book import AddressBook
from contact_book.contact_book.classes.class_notes import NoteBook
from contact_book.contact_book.classes.file_checker import FileSorter
from contact_book.contact_book.classes.decorators import bug_catcher
from os import path


def main():
    while True:
        print("\nCommand 'help' will help you.")
        data = input_user_text()
        command, name, data = parse_user_text(data)
        result = handler(command, name, data)
        show_results(result)


"""MAIN FUNCTIONS"""


@bug_catcher
def input_user_text() -> str:
    """User input."""
    data = input("Please enter what do you want to do: ")
    return data


@bug_catcher
def parse_user_text(text: str) -> list:
    """Search command and other information in user input."""

    data = text.split()
    if len(data) == 1:
        command, name, information = data[0], "", ""
    else:
        command = data[0]
        name = data[1]
        information = data[2:]
    return [command, name, information]


@bug_catcher
def handler(command: str, name: str, data: list) -> str | list:
    """Here we find signatures and call functions"""
    if command in commands:
        return commands[command](name, data)
    else:
        raise KeyError(f"Wrong command. I don't know which mean '{command}'.")


@bug_catcher
def show_results(result: str | list):
    """Print all results and information which functions return to us."""
    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(result)


"""END MAIN FUNCTIONS"""

"""CONTACTBOOK"""


@bug_catcher
def create_contact(name: str, *_) -> str:
    return book.create_new_contact(name)


@bug_catcher
def add_phone_to_contact(name: str, data: list) -> str:
    record = book[name]  # Check if this record exists
    return record.add_phone(data[0])


@bug_catcher
def add_email_to_contact(name: str, data: list) -> str:
    record = book[name]  # Check if this record exists
    return record.add_email(data[0])


@bug_catcher
def add_address_to_contact(name: str, data: list) -> str:
    record = book[name]  # Check if this record exists
    return record.add_address(" ".join(data))


@bug_catcher
def set_birthday(name: str, data: list) -> str:
    record = book[name]  # Check if this record exists
    return record.set_birthday(data[0])


@bug_catcher
def edit_contact_information(name: str, data: list) -> str:
    record = book[name]  # Check if this record exists
    field, old, new = data[0], data[1], data[2]
    return record.edit_contact_information(field, old, new)


@bug_catcher
def edit_name(old_name: str, new_name: list) -> str:
    return book.edit_contact(old_name, new_name[0])


@bug_catcher
def search_contact(name, *_) -> str:
    return book.search_contact(name)


@bug_catcher
def search_in_all_information(name: str, data: list) -> list:
    data = " ".join([name, *data])  # In function handler() all our functions take in 2 arguments, so all our other functions will take in 2 argument
    # and if we need to transform data type - we can do it in every function where we need it
    return book.search_in_all_contact_information(data)


@bug_catcher
def show_nearest_birthdays(days: str, *_) -> list:
    """Here we call information about birthdays which will happen within the next DAYS days.
    If DAYS argument is empty - default DAYS in show_upcoming_birthday() == 7"""

    if days:
        n = int(days)  # Check isinstance(days, int) and also our class method waiting for type(int)
        return book.show_upcoming_birthdays(n=n)
    else:
        return book.show_upcoming_birthdays()


@bug_catcher
def days_to_birthday(name: str, *_) -> str:
    record = book[name]  # Check if this record exists
    return record.days_to_birthday()


@bug_catcher
def days_to_birthday_for_all(*_) -> list:
    return book.days_to_birthdays_all_contacts()


@bug_catcher
def show_contacts(*_) -> list:
    return book.show_all_contacts()


@bug_catcher
def clear_book(*_) -> str:
    answer = input("You want to delete all your contacts. Are you sure? Y/N: ")
    if answer == "Y":
        return book.clear_all_book()
    else:
        return "Operation 'delete all contacts' canceled."


"""END CONTACTBOOK"""

"""NOTEBOOK"""


@bug_catcher
def create_note(name: str, info: list) -> str:
    return notes.create_new_note(name, info)


@bug_catcher
def add_note_information(name, info):
    return notes.add_note(name, info)


@bug_catcher
def clear_one_note(name, *_):
    return notes.clear_note(name)


@bug_catcher
def clear_tags(name, *_):
    return notes.clear_tags(name)


@bug_catcher
def clear_text(name, *_):
    return notes.clear_text(name)


@bug_catcher
def del_one_note(name, *_):
    return notes.del_note(name)


@bug_catcher
def search_in_text(text, *_):
    return notes.search_in_text(text)


@bug_catcher
def search_in_tags(tags, *_):
    return notes.search_in_tags(tags)


@bug_catcher
def sorted_by_tags(name, info):
    final_info = [name, *info]
    return notes.sort_by_tags(final_info)


@bug_catcher
def show_note(name, *_):
    return notes.show_note(name)


@bug_catcher
def show_note_book(*_):
    return notes.show_all()


"""END NOTEBOOK"""

"""FILE SORTER"""


@bug_catcher
def file_sorter(path_for_sorting, *_):
    one_time = FileSorter(path_for_sorting)
    one_time.job()


"""END FILE SORTER"""

"""HELP and FINAL"""


@bug_catcher
def help_me(*_):
    return "If you want to know how to use this script - use command 'instruction' with:\n" \
           "'contacts' - to read about ContactBook commands.\n" \
           "'notes' - to read about NoteBook.\n" \
           "'file' - to read about FileSorter."


@bug_catcher
def instructions(category, *_):
    if category == "contacts":
        main_path = path.join("../instructions", "contact_book.txt")
    elif category == "notes":
        main_path = path.join("../instructions", "note_book.txt")
    elif category == "file":
        main_path = path.join("../instructions", "file_sorter.txt")
    else:
        raise ValueError(f"I can't find instruction for {category}.")
    with open(main_path, "r") as file:
        result = file.read()
    return result


@bug_catcher
def good_bye(*_):
    print(book.save_to_file())
    print(notes.save_to_file())
    exit("Bye")


"""END HELP an FINAL"""

commands = {"help": help_me,
            "instruction": instructions,

            "create": create_contact,
            "add_phone": add_phone_to_contact,
            "add_email": add_email_to_contact,
            "add_address": add_address_to_contact,
            "set_birthday": set_birthday,
            "show_birthdays": show_nearest_birthdays,
            "days_to": days_to_birthday,
            "birthday_for_all": days_to_birthday_for_all,
            "edit_contact": edit_contact_information,
            "edit_name": edit_name,
            "search": search_contact,
            "search_info": search_in_all_information,
            "show": show_contacts,
            "clear_book": clear_book,

            "create_note": create_note,
            "add_note": add_note_information,
            "clear_note": clear_one_note,
            "clear_tags": clear_tags,
            "clear_text": clear_text,
            "delete_note": del_one_note,
            "search_in_text": search_in_text,
            "search_in_tags": search_in_tags,
            "sorted_by_tags": sorted_by_tags,
            "show_note": show_note,
            "show_note_book": show_note_book,

            "file_sorter": file_sorter,

            "exit": good_bye}

if __name__ == "__main__":

    book = AddressBook()
    notes = NoteBook()
    try:
        print(book.load_from_file())
    except FileNotFoundError:
        book.save_to_file()
    try:
        print(notes.load_from_file())
    except FileNotFoundError:
        notes.save_to_file()

    main()
