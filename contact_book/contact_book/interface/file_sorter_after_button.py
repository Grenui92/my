import tkinter as tk
import sys
from contact_book.contact_book.classes.file_checker import FileSorter
def main():
    absolute_folder = {'archives': ['zip', 'gz', 'tar'], 'video': ['avi', 'mp4', 'mov', 'mkv'], 'audio': ['mp3', 'ogg', 'wav', 'amr'],
                       'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'], 'images': ['jpeg', 'png', 'jpg', 'svg'], 'others': [],
                       'torrent': ['torrent'], 'programs': ['exe']}

    def new_absolute_folders_create():

        print("\nВот по таким папкам в соответствии с расширениями будут отсортированы файлы:")
        for k, v in absolute_folder.items():
            print(f'Папка {k} будет включать в себя файлы с расширением {v}')

    def add_folder_tk():
        name = add_folder_entry_name.get()
        if name not in absolute_folder:
            absolute_folder[name] = []
            print(f"Folder {name} successfully added.")
        else:
            print(f"Folder {name} already exist.")

    def add_file_extension_tk():
        name = add_file_extension_entry_name.get()
        extension = add_file_extension_entry_extens.get()
        absolute_folder[name].append(extension)
        print(f"Extension {extension} successfully added to folder {name}")
    def sort_all_tk():
        my_path = file_sorter_entry_path.get()
        work = FileSorter(path=my_path)


    window_sorter = tk.Tk()
    """WINDOW"""

    window_sorter.config(bg="#C7C6C6")
    window_sorter.title("FILE SORTER")
    window_sorter.geometry("800x600+500+250")
    window_sorter.resizable(True, True)

    """END WINDOW"""

    """BUTTON"""

    file_sorter_button = tk.Button(window_sorter, text="Sort",
                                   command=sort_all_tk,
                                   bg="#7DFF9C")
    add_folder_button = tk.Button(window_sorter, text="Add result folder:",
                           command=add_folder_tk)
    add_file_extension_button = tk.Button(window_sorter, text="Add file extension:",
                                          command=add_file_extension_tk,
                                          bg="#BEFDF5")
    show_absolute_folders_button = tk.Button(window_sorter, text="Show folders and extensions",
                                             command=new_absolute_folders_create,
                                             bg="#EAFF7D")

    """END BUTTON"""

    ####
    file_sorter_button.grid(row=2, column=0, sticky="ewns")
    path_label = tk.Label(window_sorter, text="Insert path for you system\n(Windows, Linux, MacOS)", bg="#7DFF9C")
    path_label.grid(row=0, column=0, sticky="ewns")
    file_sorter_entry_path = tk.Entry(window_sorter)
    file_sorter_entry_path.grid(row=1, column=0, sticky="ewns")

    ####
    add_folder_button.grid(row=0, column=2, sticky="ewns")
    folder_label = tk.Label(window_sorter, text="Folder name:")
    folder_label.grid(row=0, column=3, sticky="ewns")
    add_folder_entry_name = tk.Entry(window_sorter)
    add_folder_entry_name.grid(row=0, column=4, sticky="ewns")

    ####
    add_file_extension_button.grid(row=1, column=2, sticky="ew")
    folder_label = tk.Label(window_sorter, text="Folder name:", bg="#BEFDF5")
    folder_label.grid(row=1, column=3, sticky="ewns")
    add_file_extension_entry_name = tk.Entry(window_sorter)
    add_file_extension_entry_name.grid(row=1, column=4, sticky="ewns")
    file_label = tk.Label(window_sorter, text="File extension:", bg="#BEFDF5")
    file_label.grid(row=2, column=3, sticky="ewns")
    add_file_extension_entry_extens = tk.Entry(window_sorter)
    add_file_extension_entry_extens.grid(row=2, column=4, sticky="ewns")

    ####
    show_absolute_folders_button.grid(row=0, column=1, rowspan=4, sticky="ewns")


    def redirect(string):
        text_window.insert(tk.INSERT, string)

    sys.stdout.write = redirect
    text_window = tk.Text(window_sorter, bg="black", foreground="white", wrap="word")
    text_window.grid(columnspan=5, sticky="ewns")
    new_absolute_folders_create()

    window_sorter.mainloop()

if __name__ == "__main__":
    main()