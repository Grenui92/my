from pickle import dump, load
from collections import UserDict
import os


class NoteBook(UserDict):

    __instance = None

    def __new__(cls):
        """Singltone????"""
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, file_path=os.path.join("files", "node_book.bin")):
        super().__init__()
        self.file_path = file_path

    def create_new_note(self, title: str, text: str) -> str:
        if title not in self.data:
            tags = []
            for piece in text.split():  # Search tags in all text
                if piece.startswith("#"):
                    tags.append(piece)
            self.data[title] = Note(title, tags, text)
            return f"Note with name {title} successfully create."
        else:
            raise KeyError(f"Note with name {title} already exist.")

    def add_note(self, title: str, text: str) -> str:
        tags = []
        for piece in text.split():  # Ищем теги в тексте, именно так они добавляются изначально
            if piece.startswith("#"):
                tags.append(piece)
        self.data[title].add_content(tags, text)
        return f"Information successfully added to {title}."

    def clear_note(self, title: str) -> str:
        self.data[title].clear_tags()
        self.data[title].clear_text()
        return f"Note named {title} successfully cleared."

    def clear_text(self, title: str) -> str:
        self.data[title].clear_text()
        return f"Text in {title} cleared."

    def clear_tags(self, title: str) -> str:
        self.data[title].clear_tags()
        return f"Tags in {title} cleared."

    def del_note(self, title: str) -> str:
        del self.data[title]
        return f"Note named {title} successfully deleted."

    def search_in_text(self, info: str) -> list:
        result = []
        for note in self.data.values():
            if info in note.text or info == note.name:
                if not result:
                    result = [f"Search results for {info} in text:\n"]
                result.append(f"\nName: {note.name}\n"
                              f"Tags: {note.tags}\n"
                              f"Text: {note.text}\n")
        return result if result else [f"Search results for {info} in text:\nEmpty"]

    def search_in_tags(self, info: str) -> list:
        result = []
        for note in self.data.values():
            if info in note.tags or info == note.name:
                if not result:
                    result = [f"Search results for {info} in text:\n"]
                result.append(f"\nName: {note.name}\n"
                              f"Tags: {note.tags}\n"
                              f"Text: {note.text}\n")
        return result if result else [f"Search results for {info} in text:\nEmpty"]

    def show_note(self, title: str) -> str:
        note = self.data[title]
        return f"\nName: {note.name}\n" \
               f"Tags: {note.tags}\n" \
               f"Text: {note.text}\n"

    def show_all(self) -> list:
        result = []
        for name, note in self.data.items():
            result.append(f"\nName: {note.name}\n"
                          f"Tags: {note.tags}\n"
                          f"Text: {note.text}\n")
        return result

    def sort_by_tags(self, tags: list) -> list:
        result = []
        for note in self.data.values():
            cnt = 0
            for tag in tags:  # Считаем сколько раз сумарно встречается каждый элемент из списка тегов в тегах записи
                if tag in note.tags:
                    cnt += 1 if tag in note.tags else 0
            result.append(f"Coincidences with tags {[i for i in tags if i]}: {cnt}\n" 
                          f"\nName: {note.name}\n"
                          f"Tags: {note.tags}\n"
                          f"Text: {note.text}\n")
        return sorted(result, reverse=True)


    def clear_all_book(self):
        self.data.clear()
        return f"Book successfully cleared."

    def save_to_file(self) -> str:
        with open(self.file_path, "wb") as file:
            dump(self.data, file)
        return f"Successfully save NoteBook to file {self.file_path}"

    def load_from_file(self) -> str:
        with open(self.file_path, "rb") as file:
            self.data = load(file)
        return f"Successfully load NoteBook from file {self.file_path}"


class Note:

    def __init__(self, name: str, tags: list, text: str):
        self.name = name
        self._tags = None
        self.tags = tags
        self.text = text

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if len(value) < 1:
            self._tags = []
        else:
            self._tags = [*value]

    def add_content(self, tags, text):
        if tags:
            self.tags.extend(tags)
        if text:
            self.text += text + " "

    def clear_text(self):
        self.text = ""

    def clear_tags(self):
        self._tags = []
