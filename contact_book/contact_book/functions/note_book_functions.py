
# def create_note(name: str, info: list) -> str:
#     return notes.create_new_note(name, info)
def add_note_information(name, info):
    return notes.add_note(name, info)
def clear_one_note(name, *_):
    return notes.clear_note(name)
def clear_tags(name, *_):
    return notes.clear_tags(name)
def clear_text(name, *_):
    return notes.clear_text(name)
def del_one_note(name, *_):
    return notes.del_note(name)
def search_in_text(text, *_):
    return notes.search_in_text(text)
def search_in_tags(tags, *_):
    return notes.search_in_tags(tags)
def sorted_by_tags(name, info):
    final_info = [name, *info]
    return notes.sort_by_tags(final_info)
def show_note(name, *_):
    return notes.show_note(name)

def show_note_book(*_):
    return notes.show_all()