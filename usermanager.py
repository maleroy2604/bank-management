import os.path

from filemanager import FileManager


class UserManager:
    def __init__(self, user_file_name):
        self._user_file = user_file_name

    def add_user(self, user):
        if not os.path.exists(self._user_file):
            FileManager.create_file(self._user_file)
        FileManager.save_to_file(user, self._user_file)

    def get_user_from_file(self):
        if os.path.exists(self._user_file):
            return FileManager.load_from_file(self._user_file)
        else:
            raise ValueError(f"{self._user_file} does not exist")
