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