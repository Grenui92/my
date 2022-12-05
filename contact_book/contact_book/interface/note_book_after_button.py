import tkinter as tk
import sys
from contact_book.contact_book.classes.class_notes import NoteBook, Note
from contact_book.contact_book.classes.decorators import bug_catcher

def main():
    note = NoteBook()
    try:
        note.load_from_file()
    except FileNotFoundError:
        note.save_to_file()

    @bug_catcher
    def create():
        pass

    note_window = tk.Tk()

    """WINDOW"""

    note_window.command()
    note_window.config(bg="#C7C6C6")
    note_window.title("CONTACT BOOK")
    note_window.geometry("1220x930+300+50")
    note_window.resizable(False, True)
    note_window.grid_columnconfigure(0, minsize=250)
    note_window.grid_columnconfigure(4, minsize=200)
    """END WINDOW"""

    """END BUTTON"""
    def redirector(input_str):
        text.insert(tk.INSERT, input_str)

    sys.stdout.write = redirector
    text = tk.Text(note_window, bg="#000000", foreground="white")
    text.grid(columnspan=9, sticky="ew")
    note_window.mainloop()

if __name__ == "__main__":
    main()