import sys
import tkinter as tk
from contact_book.contact_book.classes.class_contact_book import AddressBook
from contact_book.contact_book.classes.class_record import Record
from contact_book.contact_book.classes.decorators import bug_catcher


def main():
    book = AddressBook()
    try:
        book.load_from_file()
    except FileNotFoundError:
        book.save_to_file()

    @bug_catcher
    def create_contact():
        name = create_contact_entry.get()
        print(book.create_new_contact(name=name))

    @bug_catcher
    def add_phone_to_contact():
        name = add_phone_to_contact_entry_name.get()
        phone = add_phone_to_contact_entry_phone.get()
        record: Record = book[name]
        print(record.add_phone(phone=phone))

    @bug_catcher
    def add_email_to_contact():
        name = add_email_to_contact_entry_name.get()
        email = add_email_to_contact_entry_email.get()
        record: Record = book[name]
        print(record.add_email(email=email))

    @bug_catcher
    def add_address_to_contact():
        name = add_address_to_contact_entry_name.get()
        address = add_address_to_contact_entry_address.get()
        record: Record = book[name]
        print(record.add_address(address=address))

    @bug_catcher
    def set_birthday():
        name = set_birthday_entry_name.get()
        birthday_date = set_birthday_entry_date.get()
        record: Record = book[name]
        print(record.set_birthday(date_b=birthday_date))

    @bug_catcher
    def edit_contact_information():
        name = edit_contact_information_entry_name.get()
        field = edit_contact_information_entry_field.get()
        old = edit_contact_information_entry_old.get()
        new = edit_contact_information_entry_new.get()
        record: Record = book[name]
        print(record.edit_contact_information(field=field, old=old, new=new))

    @bug_catcher
    def edit_name():
        old_name = edit_name_entry_name.get()
        new_name = edit_name_entry_new_name.get()
        print(book.edit_contact(old_name=old_name, new_name=new_name))

    @bug_catcher
    def search_contact():
        name = search_contact_entry_name.get()
        print(book.search_contact(name=name))

    @bug_catcher
    def search_in_all_information():
        information = search_in_all_information_entry_information.get()
        print(book.search_in_all_contact_information(search=information))

    @bug_catcher
    def show_nearest_birthdays():
        days = show_nearest_birthdays_entry_days.get() if show_nearest_birthdays_entry_days.get() else 7
        result = book.show_upcoming_birthdays(n=days)
        if result:
            for contact in result:
                print(contact)
        else:
            print(f"No birthdays in nearest {days} days")

    @bug_catcher
    def days_to_birthday():
        name = days_to_birthday_entry_name.get()
        record: Record = book[name]
        print(record.days_to_birthday())

    @bug_catcher
    def days_to_birthday_for_all():
        result = book.days_to_birthdays_all_contacts()
        for contact in result:
            print(contact)

    @bug_catcher
    def show_contacts():
        result = book.show_all_contacts()
        for contact in result:
            print(contact)

    @bug_catcher
    def clear_one_contact():
        name = clear_one_contact_entry_name.get()
        field = clear_one_contact_entry_field.get() if clear_one_contact_entry_field.get() else None
        sure = clear_one_contact_entry_sure.get()
        if sure.upper() == "Y":
            print(book.clear_contact(name=name, field=field))
        else:
            print("Clearing canceled.")

    @bug_catcher
    def clear_book():
        answer = clear_book_entry_sure.get()
        if answer == "Y":
            print(book.clear_all_book())
        else:
            print("Clearing canceled.")

    def save_to_file():
        print(book.save_to_file())

    window_con = tk.Tk()

    """WINDOW"""
    window_con.command()
    window_con.config(bg="#C7C6C6")
    window_con.title("CONTACT BOOK")
    window_con.geometry("1220x930+300+50")
    window_con.resizable(False, True)
    window_con.grid_columnconfigure(0, minsize=250)
    window_con.grid_columnconfigure(4, minsize=200)
    """END WINDOW"""
    """BUTTONS"""
    create_contact_button = tk.Button(window_con, text="Create NEW contact",
                                      command=create_contact)
    add_phone_to_contact_button = tk.Button(window_con, text="Add phone to contact",
                                            command=add_phone_to_contact)
    add_email_to_contact_button = tk.Button(window_con, text="Add email to contact",
                                            command=add_email_to_contact)
    add_address_to_contact_button = tk.Button(window_con, text="Add address to contact",
                                              command=add_address_to_contact)
    set_birthday_button = tk.Button(window_con, text="Set birthday to contact",
                                    command=set_birthday)
    edit_contact_information_button = tk.Button(window_con, text="Edit contact information",
                                                command=edit_contact_information)
    edit_name_button = tk.Button(window_con, text="Edit contact name",
                                 command=edit_name)
    search_contact_button = tk.Button(window_con, text="Search one contact",
                                      command=search_contact)
    search_in_all_information_button = tk.Button(window_con, text="Search in all contacts information",
                                                 command=search_in_all_information)
    show_nearest_birthdays_button = tk.Button(window_con, text="Show nearest birthday",
                                              command=show_nearest_birthdays)
    days_to_birthday_button = tk.Button(window_con, text="Days to birthday for one contact",
                                        command=days_to_birthday)
    days_to_birthday_for_all_button = tk.Button(window_con, text="Days to birthday for all",
                                                command=days_to_birthday_for_all)
    show_contacts_button = tk.Button(window_con, text="Show Contact Book",
                                     command=show_contacts)
    clear_one_contact_button = tk.Button(window_con, text="Clear ONE contact",
                                         command=clear_one_contact)
    clear_book_button = tk.Button(window_con, text="Clear Contact Book",
                                  command=clear_book)
    save_to_file_button = tk.Button(window_con, text="Save Contact Book",
                                    command=save_to_file,
                                    bg="#FDA7A7")
    did_you_save = tk.Button(window_con, text="DID YOU SAVE YOUR BOOK?!?!?!? \n press her if you want to save",
                             command=save_to_file,
                             bg="red", font=500)

    """END BUTTONS"""
    """BUTTONS GRID"""

    create_contact_button.grid(sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=0, column=1)
    create_contact_entry = tk.Entry(window_con, width=10)
    create_contact_entry.grid(row=0, column=2)

    search_contact_button.grid(sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=1, column=1)
    search_contact_entry_name = tk.Entry(window_con, width=10)
    search_contact_entry_name.grid(row=1, column=2)

    add_phone_to_contact_button.grid(row=3, sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=3, column=1)
    add_phone_to_contact_entry_name = tk.Entry(window_con, width=10)
    add_phone_to_contact_entry_name.grid(row=3, column=2)
    label_phone = tk.Label(window_con, text="Phone:")
    label_phone.grid(row=3, column=3, sticky="ew")
    add_phone_to_contact_entry_phone = tk.Entry(window_con)
    add_phone_to_contact_entry_phone.grid(row=3, column=4, sticky="ew")

    add_email_to_contact_button.grid(sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=4, column=1)
    add_email_to_contact_entry_name = tk.Entry(window_con, width=10)
    add_email_to_contact_entry_name.grid(row=4, column=2)
    label_phone = tk.Label(window_con, text="Email:")
    label_phone.grid(row=4, column=3, sticky="ew")
    add_email_to_contact_entry_email = tk.Entry(window_con)
    add_email_to_contact_entry_email.grid(row=4, column=4, sticky="ew")

    add_address_to_contact_button.grid(sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=5, column=1)
    add_address_to_contact_entry_name = tk.Entry(window_con, width=10)
    add_address_to_contact_entry_name.grid(row=5, column=2)
    label_phone = tk.Label(window_con, text="Address:")
    label_phone.grid(row=5, column=3, sticky="ew")
    add_address_to_contact_entry_address = tk.Entry(window_con)
    add_address_to_contact_entry_address.grid(row=5, column=4, sticky="ew")

    set_birthday_button.grid(sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=6, column=1)
    set_birthday_entry_name = tk.Entry(window_con, width=10)
    set_birthday_entry_name.grid(row=6, column=2)
    label_phone = tk.Label(window_con, text="Date:")
    label_phone.grid(row=6, column=3, sticky="ew")
    set_birthday_entry_date = tk.Entry(window_con)
    set_birthday_entry_date.grid(row=6, column=4, sticky="ew")

    edit_contact_information_button.grid(row=12, sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=12, column=1)
    edit_contact_information_entry_name = tk.Entry(window_con, width=10)
    edit_contact_information_entry_name.grid(row=12, column=2)

    label_filed = tk.Label(window_con, text="Field:")
    label_filed.grid(row=12, column=3, sticky="ew")
    edit_contact_information_entry_field = tk.Entry(window_con)
    edit_contact_information_entry_field.grid(row=12, column=4, sticky="ew")

    label_old = tk.Label(window_con, text="Old information:")
    label_old.grid(row=12, column=5)
    edit_contact_information_entry_old = tk.Entry(window_con)
    edit_contact_information_entry_old.grid(row=12, column=6)

    label_new = tk.Label(window_con, text="New information:")
    label_new.grid(row=12, column=7)
    edit_contact_information_entry_new = tk.Entry(window_con)
    edit_contact_information_entry_new.grid(row=12, column=8)

    edit_name_button.grid(row=7, sticky="ew")
    label_name = tk.Label(window_con, text="Name:")
    label_name.grid(row=7, column=1)
    edit_name_entry_name = tk.Entry(window_con, width=10)
    edit_name_entry_name.grid(row=7, column=2)
    label_new_name = tk.Label(window_con, text="New name:")
    label_new_name.grid(row=7, column=3, sticky="ew")
    edit_name_entry_new_name = tk.Entry(window_con)
    edit_name_entry_new_name.grid(row=7, column=4, sticky="ew")

    search_in_all_information_button.grid(row=8, sticky="ew")
    label_filed = tk.Label(window_con, text="Search Information:")
    label_filed.grid(row=8, column=1, columnspan=2, sticky="ew")
    search_in_all_information_entry_information = tk.Entry(window_con)
    search_in_all_information_entry_information.grid(row=8, column=3, columnspan=2, sticky="ew")

    show_nearest_birthdays_button.grid(row=9, sticky="ew")
    label_filed = tk.Label(window_con, text="How many days you want to see:")
    label_filed.grid(row=9, column=1, columnspan=3, sticky="ew")
    show_nearest_birthdays_entry_days = tk.Entry(window_con)
    show_nearest_birthdays_entry_days.grid(row=9, column=4, sticky="ew")

    days_to_birthday_button.grid(row=2, sticky="ew")
    label_name = tk.Label(text="Name:")
    label_name.grid(row=2, column=1, sticky="ew")
    days_to_birthday_entry_name = tk.Entry(window_con, width=10)
    days_to_birthday_entry_name.grid(row=2, column=2)

    clear_one_contact_button.grid(row=10, sticky="ew")
    label_name = tk.Label(text="Name:")
    label_name.grid(row=10, column=1)
    clear_one_contact_entry_name = tk.Entry(window_con, width=10)
    clear_one_contact_entry_name.grid(row=10, column=2, sticky="ew")
    label_field = tk.Label(text="Field (if empty - it will clear ALL fields):")
    label_field.grid(row=10, column=3, columnspan=2, sticky="ew")
    clear_one_contact_entry_field = tk.Entry(window_con, width=10)
    clear_one_contact_entry_field.grid(row=10, column=5, sticky="ew")
    label_sure = tk.Label(text="Are you sure that you want to clear? Y/N:")
    label_sure.grid(row=10, column=6, columnspan=2, sticky="ew")
    clear_one_contact_entry_sure = tk.Entry(window_con)
    clear_one_contact_entry_sure.grid(row=10, column=8, sticky="ew")

    clear_book_button.grid(row=11, sticky="ew")
    label_filed = tk.Label(text="Are you sure?! This button will delete all information from Contact Book! Y/N:")
    label_filed.grid(row=11, column=1, columnspan=5, sticky="ew")
    clear_book_entry_sure = tk.Entry(window_con, width=10)
    clear_book_entry_sure.grid(row=11, column=6, sticky="w")

    show_contacts_button.grid(row=13, column=1, columnspan=3, sticky="ew")
    days_to_birthday_for_all_button.grid(row=13, column=4, sticky="ew")

    did_you_save.grid(row=0, column=5, rowspan=3, columnspan=4, sticky="ewsn")

    save_to_file_button.grid(row=13, column=0, sticky="ew")

    def redirector(input_str):
        text.insert(tk.INSERT, input_str)

    sys.stdout.write = redirector
    text = tk.Text(window_con, bg="#000000", foreground="white")
    text.grid(columnspan=9, sticky="ew")
    """END BUTTONS GRID"""

    window_con.mainloop()


if __name__ == "__main__":
    main()
