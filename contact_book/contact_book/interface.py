import tkinter as tk
from os import path
import contact_book.contact_book.interface.contact_book_after_button as cont_but_main
import contact_book.contact_book.interface.note_book_after_button as note_but_main
import contact_book.contact_book.interface.file_sorter_after_button as file_but_main

window = tk.Tk()

"""WINDOW"""
photo = tk.PhotoImage(file="interface/corner_icon.png")
window.iconphoto(False, photo)
window.config(bg="#C7C6C6")
window.title("Your own pocket helper")
window.geometry("600x50+400+150")
window.resizable(False, False)
window.grid_rowconfigure(0, minsize=50)
window.grid_columnconfigure(0, minsize=200)
window.grid_columnconfigure(1, minsize=200)
window.grid_columnconfigure(2, minsize=200)
"""END WINDOW"""

"""CONTACT_BOOK_BUTTON"""
contact_book_button = tk.Button(window,
                                text="CONTACT BOOK",
                                command=cont_but_main.main,
                                bg="#C1F8FF")

"""NOTE_BOOK_BUTTON"""
note_book_button = tk.Button(window,
                             text="NOTE BOOK",
                             command=note_but_main.main,
                             bg="#FFFF5A")

"""FILE_SORTER_BUTTON"""
file_sorter_button = tk.Button(window,
                               text="FILE SORTER",
                               command=file_but_main.main,
                               bg="#FFC1C1")
"""BUTTONS GRID"""
contact_book_button.grid(row=0, column=0, sticky="nswe")
note_book_button.grid(row=0, column=1, sticky="nswe")
file_sorter_button.grid(row=0, column=2, sticky="nswe")

window.mainloop()
