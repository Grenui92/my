import shutil
import pathlib
import os
from datetime import datetime


class FileSorter:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        if not self.path.is_dir():
            raise FileExistsError(f"Wrong path: {self.path}")
        self.i_know = set()
        self.files_list = {}
        self.absolute_folders = self.new_absolute_folders_create()
        self.translate_map: dict = self.__new_translate_map()

    def job(self):
        """Main function of sorting files"""
        self.file_checking(self.path)
        self.show_results()

    def file_checking(self, path) -> (list, list, dict):
        """Основная функция сортировки в которой будем бежать по файлам, рекурсировать, если будут вложенные папки, и выполнять сортировку"""

        p = pathlib.Path(path)
        for item in p.iterdir():
            if item.is_dir() and item.name not in self.absolute_folders:
                self.if_is_dir(path=p, item=item)
                self.delete_other_dir(p=p)
            elif item.is_file():
                self.if_is_file(item=item)

    def show_results(self):
        """Выведение результата всех операций. Списков расширений."""

        print(
            f"Это расширения файлов, которые я знаю: {[extensions for extensions in self.absolute_folders.values() if extensions]}, "
            f"а это известные расширения, которые я встретил только что: {self.i_know}")
        print(f"А эти расширения я не знаю, потому отправил их в папку 'others': {self.absolute_folders['others']}")
        for directs in self.files_list:
            print(directs, *self.files_list[directs], sep='\n\t')

    def if_is_dir(self, path, item):
        self.file_checking(os.path.join(path, item.name))
        new_name = self.normalize(item.name)
        item.rename(os.path.join(path, new_name))

    def if_is_file(self, item):
        new_name = self.normalize(item.stem)
        now_time = datetime.now().time().microsecond
        for k, v in self.absolute_folders.items():
            if item.suffix[1:] in v:
                self.create_new_folder_(k)
                if k == 'archives':
                    try:
                        shutil.unpack_archive(item, extract_dir=os.path.join(self.path, "archives", item.stem), format=f'{item.suffix[1:]}')
                    except RuntimeError:
                        print(f"Извините, этот архив {item.name} требует пароль.")
                    self.file_renamer(item=item, main_path_rename=self.path, k=k, new_name=new_name, now_time=now_time)
                    self.files_list.setdefault('archives', []).append(f'{new_name}{item.suffix}')
                    break
                else:
                    self.file_renamer(item=item, main_path_rename=self.path, k=k, new_name=new_name, now_time=now_time)
                    self.i_know.add(item.suffix)
                    self.files_list.setdefault(k, []).append(f'{new_name}{item.suffix}')
                    break
        else:
            self.create_new_folder_("others")
            self.file_renamer(item=item, main_path_rename=self.path, k="others", new_name=new_name, now_time=now_time)
            self.files_list.setdefault("others", []).append(f'{new_name}{item.suffix}')
            self.absolute_folders.setdefault("others", []).append(item.suffix)

    @staticmethod
    def delete_other_dir(p):
        for item in p.iterdir():
            try:
                item.rmdir()
            except FileNotFoundError:
                pass
            except OSError:
                pass


    def file_renamer(self, item, main_path_rename, k, new_name, now_time):
        try:
            item.rename(os.path.join(main_path_rename, k, f"{new_name}{item.suffix}"))
        except FileExistsError:
            item.rename(os.path.join(main_path_rename, k, f"{new_name}{now_time}{item.suffix}"))


    def normalize(self, name: str) -> str:
        """По идее должна вызываться из функции file_checking() весте с именем, которое мы будем обрабатывать.
        Вернет уже обработанное имя и само переименование уже будет происходить в file_checking(). Вызывается много раз, на каждый файл."""

        name = name.translate(self.translate_map)
        for i in name:
            if not i.isalnum():
                name = name.replace(i, '_')
        return name

    def create_new_folder_(self, folder_name):
        try:
            os.mkdir(os.path.join(self.path, folder_name))
        except FileExistsError:
            pass


    def __new_translate_map(self) -> dict:
        translated_map = {1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1045: 'E', 1046: 'GH', 1047: 'Z',
                          1048: 'I', 1049: 'J', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
                          1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'H', 1062: 'TS', 1063: 'CH',
                          1064: 'SH', 1065: 'SH', 1066: '', 1067: 'I', 1068: '', 1069: 'E', 1070: 'YU', 1071: 'YA',
                          1025: 'YO', 1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1077: 'e', 1078: 'gh',
                          1079: 'z', 1080: 'i', 1081: 'j', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o',
                          1087: 'p', 1088: 'r', 1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'h', 1094: 'ts',
                          1095: 'ch', 1096: 'sh', 1097: 'sh', 1098: '', 1099: 'i', 1100: '', 1101: 'e', 1102: 'yu',
                          1103: 'ya', 1105: 'yo', 105: 'i', 1031: 'ji', 1169: 'g'}
        return translated_map

    @staticmethod
    def new_absolute_folders_create():

        print("Вот по таким папкам в соответствии с расширениями будут отсортированы файлы:")
        for k, v in absolute_folder.items():
            print(f'Папка {k} будет включать в себя файлы с расширением {v}')

    def add_folder(self, name: str):
        if name not in self.absolute_folders:
            self.absolute_folders[name] = []
            return f"Folder {name} successfully added."
        else:
            return f"Folder {name} already exist."

    def add_file_extension(self, name: str, extension: str):
        self.absolute_folders[name].append(extension)
        return f"Extension {extension} successfully added to folder {name}"







# absolute_folders: dict = new_absolute_folders_create()
# translate_map: dict = new_translate_map()
# main_path: str = "/home/Grenui92/Documents/Python/team_project/Downloads"

