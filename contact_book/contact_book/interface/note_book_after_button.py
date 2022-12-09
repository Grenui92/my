import tkinter as tk
import sys
from contact_book.contact_book.classes.class_notes import NoteBook
from contact_book.contact_book.classes.decorators import bug_catcher


def main():
    note_book = NoteBook()
    # try:
    #     note_book.load_from_file()
    # except FileNotFoundError:
    #     note_book.save_to_file()

    """FUNCTIONS"""

    @bug_catcher
    def create_new_note_tk():
        print(create_note_entry_text)
        title = create_note_entry_title.get()
        text = create_note_entry_text.get(index1="1.0", index2="end-1c")
        print(note_book.create_new_note(title=title, text=text))

    @bug_catcher
    def add_information_to_note_tk():
        title = add_note_entry_title.get()
        text = add_note_entry_text.get(0, -1)
        print(note_book.add_note(title=title, text=text))

    @bug_catcher
    def clear_one_note_tk():
        title = clear_one_note_entry_title.get()
        print(note_book.clear_note(title=title))

    @bug_catcher
    def clear_tags_tk():
        title = clear_tags_entry_title.get()
        print(note_book.clear_tags(title=title))

    @bug_catcher
    def clear_text_tk():
        title = clear_text_entry_title.get()
        print(note_book.clear_text(title=title))

    @bug_catcher
    def del_note_tk():
        title = del_note_entry_title.get()
        print(note_book.del_note(title=title))

    @bug_catcher
    def search_in_text_tk():
        text = search_in_text_entry_text.get()
        for note in note_book.search_in_text(info=text):
            print(note)

    @bug_catcher
    def search_in_tags_tk():
        tags = search_in_tags_entry_tags.get()
        if not tags.startswith("#"):
            print(f"Word '{tags}' not start with '#'. If you want to search in tags - you have to use '#'")
            return
        for note in note_book.search_in_tags(info=tags):
            print(note)

    @bug_catcher
    def sort_by_tags_tk():
        tags = sort_by_tags_entry_tags.get().split()
        for word in tags:
            if not word.startswith("#"):
                print(f"Word '{tags}' not start with '#'. If you want to search in tags - you have to use '#'")
                return
        for note in note_book.sort_by_tags(tags=tags):
            print(note)

    @bug_catcher
    def show_one_note_tk():
        title = show_note_entry_title.get()
        print(note_book.show_note(title=title))

    @bug_catcher
    def show_all_note_book():
        for note in note_book.show_all():
            print(note)

    @bug_catcher
    def clear_all_book_tk():
        answer = clear_all_note_book_entry_answer.get()
        if answer.upper() == "Y":
            print(note_book.clear_all_book())
        else:
            print("All book clearing canceled.")

    @bug_catcher
    def save_to_file_tk():
        print(note_book.save_to_file())

    """END FUNCTIONS"""

    """WINDOW"""

    note_window = tk.Tk()
    note_window.command()
    note_window.config(bg="#FFFF99")
    note_window.title("NOTE BOOK")
    note_window.geometry("886x782+300+50")
    note_window.resizable(False, True)
    note_window.grid_columnconfigure(0, minsize=160)
    note_window.grid_columnconfigure(4, minsize=200)
    note_window.grid_rowconfigure(0, minsize=50)

    """END WINDOW"""
    """BUTTONS"""

    create_note_button = tk.Button(note_window, text="Create note",
                                   bg="#98FD6C",
                                   command=create_new_note_tk)
    add_note_information_button = tk.Button(note_window, text="Add Information\nto note",
                                            bg="#98FD6C",
                                            command=add_information_to_note_tk)
    clear_one_note_button = tk.Button(note_window, text="Clear ONE note",
                                      bg="#FFBDBD",
                                      command=clear_one_note_tk)
    clear_tags_button = tk.Button(note_window, text="Clear tags",
                                  bg="#FFBDBD",
                                  command=clear_tags_tk)
    clear_text_button = tk.Button(note_window, text="Clear text",
                                  bg="#FFBDBD",
                                  command=clear_text_tk)
    del_note_button = tk.Button(note_window, text="Delete ONE note",
                                bg="#FFBDBD",
                                command=del_note_tk)
    search_in_text_button = tk.Button(note_window, text="Search in TEXT",
                                      bg="#ABFFF2",
                                      command=search_in_text_tk)
    search_in_tags_button = tk.Button(note_window, text="Search in TAGS",
                                      bg="#ABFFF2",
                                      command=search_in_tags_tk)
    sort_by_tags_button = tk.Button(note_window, text="Sort by tags",
                                    bg="#ABFFF2",
                                    command=sort_by_tags_tk)
    show_note_button = tk.Button(note_window, text="Show one current note",
                                 bg="#ABFFF2",
                                 command=show_one_note_tk)
    show_all_note_book = tk.Button(note_window, text="Show all Note Book",
                                   bg="#98FD6C",
                                   command=show_all_note_book)
    clear_all_note_book_button = tk.Button(note_window, text="Clear all book",
                                           bg="red",
                                           command=clear_all_book_tk)
    save_to_file_button = tk.Button(note_window, text="Save to file",
                                    bg="green",
                                    command=save_to_file_tk)
    """END BUTTONS"""
    """BUTTONS, LABEL and ENTRY GRID"""

    ####
    create_note_button.grid(row=0, column=0, sticky="ewns")
    label_title = tk.Label(note_window, text="Title:", bg="#98FD6C")
    label_title.grid(row=0, column=1, sticky="ewns")
    create_note_entry_title = tk.Entry(note_window)
    create_note_entry_title.grid(row=0, column=2, sticky="ewns")
    label_text = tk.Label(note_window, text="Text:", bg="#98FD6C")
    label_text.grid(row=0, column=3, sticky="ewns")
    create_note_entry_text = tk.Text(note_window, width=2, height=2)
    create_note_entry_text.grid(row=0, column=4, sticky="ewns")

    ####
    add_note_information_button.grid(row=1, column=0, sticky="ewns")
    label_title = tk.Label(note_window, text="Title:", bg="#98FD6C")
    label_title.grid(row=1, column=1, sticky="ewns")
    add_note_entry_title = tk.Entry(note_window)
    add_note_entry_title.grid(row=1, column=2, sticky="ewns")
    label_text = tk.Label(note_window, text="Text:", bg="#98FD6C")
    label_text.grid(row=1, column=3, sticky="ewns")
    add_note_entry_text = tk.Text(note_window, width=2, height=2)
    add_note_entry_text.grid(row=1, column=4, sticky="ewns")

    ####
    show_all_note_book.grid(row=2, column=0, columnspan=5, sticky="ewns")

    ####
    clear_one_note_button.grid(row=3, column=0, sticky="ew")
    label_title = tk.Label(note_window, text="Title:", bg="#FFBDBD")
    label_title.grid(row=4, column=0, sticky="ew")
    clear_one_note_entry_title = tk.Entry(note_window)
    clear_one_note_entry_title.grid(row=5, column=0, sticky="ew")

    ####
    clear_tags_button.grid(row=3, column=1, sticky="ew")
    label_title = tk.Label(note_window, text="Title:", bg="#FFBDBD")
    label_title.grid(row=4, column=1, sticky="ew")
    clear_tags_entry_title = tk.Entry(note_window)
    clear_tags_entry_title.grid(row=5, column=1, sticky="ew")

    ####
    clear_text_button.grid(row=3, column=2, sticky="ew")
    label_title = tk.Label(note_window, text="Title:", bg="#FFBDBD")
    label_title.grid(row=4, column=2, sticky="ew")
    clear_text_entry_title = tk.Entry(note_window)
    clear_text_entry_title.grid(row=5, column=2, sticky="ew")

    ####
    del_note_button.grid(row=3, column=3, sticky="ew")
    label_title = tk.Label(note_window, text="Title:", bg="#FFBDBD")
    label_title.grid(row=4, column=3, sticky="ew")
    del_note_entry_title = tk.Entry(note_window)
    del_note_entry_title.grid(row=5, column=3, sticky="ew")

    ####
    clear_all_note_book_button.grid(row=3, column=4, sticky="ew")
    label_answer = tk.Label(note_window, text="ARE YOU SURE?! Y/N", bg="red")
    label_answer.grid(row=4, column=4, sticky="ew")
    clear_all_note_book_entry_answer = tk.Entry(note_window)
    clear_all_note_book_entry_answer.grid(row=5, column=4, sticky="ew")

    ####
    search_in_text_button.grid(row=6, column=0, sticky="ew")
    label_text = tk.Label(note_window, text="Search text:", bg="#ABFFF2")
    label_text.grid(row=7, column=0, sticky="ewns")
    search_in_text_entry_text = tk.Entry(note_window)
    search_in_text_entry_text.grid(row=8, column=0, sticky="ew")

    ####
    search_in_tags_button.grid(row=6, column=1, sticky="ew")
    label_text = tk.Label(note_window, text="Search tags:", bg="#ABFFF2")
    label_text.grid(row=7, column=1, sticky="ewns")
    search_in_tags_entry_tags = tk.Entry(note_window)
    search_in_tags_entry_tags.grid(row=8, column=1, sticky="ew")

    ####
    sort_by_tags_button.grid(row=6, column=2, sticky="ew")
    label_tags = tk.Label(note_window, text="Tags. You can write\nlike this '#first #second etc':", bg="#ABFFF2")
    label_tags.grid(row=7, column=2, sticky="ewns")
    sort_by_tags_entry_tags = tk.Entry(note_window)
    sort_by_tags_entry_tags.grid(row=8, column=2, sticky="ew")

    ####
    show_note_button.grid(row=6, column=3, sticky="ew")
    label_title = tk.Label(note_window, text="Title:", bg="#ABFFF2")
    label_title.grid(row=7, column=3, sticky="ewns")
    show_note_entry_title = tk.Entry(note_window)
    show_note_entry_title.grid(row=8, column=3, sticky="ew")

    ####
    save_to_file_button.grid(row=6, column=4, rowspan=3, sticky="ewns")

    """END BUTTONS, LABEL AND ENTRY GRID"""

    def redirector(input_str):
        text_print.insert(tk.INSERT, input_str)

    sys.stdout.write = redirector
    text_print = tk.Text(note_window, bg="#000000", foreground="white")
    text_print.grid(columnspan=9, sticky="ew")
    note_window.mainloop()


if __name__ == "__main__":
    main()
