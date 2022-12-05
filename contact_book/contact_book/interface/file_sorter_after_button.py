import tkinter as tk
from os import  path
def main():
    window = tk.Tk()

    """WINDOW"""

    window.config(bg="#C7C6C6")
    window.title("FILE SORTER")
    window.geometry("800x600+500+250")
    window.resizable(False, False)
    """END EINDOW"""
    window.mainloop()

if __name__ == "__main__":
    main()