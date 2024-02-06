import os.path
import unittest

from session import Session
from user import User
from filemanager import FileManager
from usermanager import UserManager


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._user = User(0, 'joe', '7D2d69881*', [], 'admin')
        self._filename = "user-test.txt"

    def tearDown(self) -> None:
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def test_file_manager(self):
        FileManager.create_file(self._filename)
        FileManager.save_to_file(self._user, self._filename)
        actual_user = FileManager.load_from_file(self._filename)
        list_of_user_excepted = [self._user]
        self.assertEqual(actual_user,list_of_user_excepted )

    def test_create_file(self):
        FileManager.create_file(self._filename)
        file_exist = os.path.exists(self._filename)
        self.assertEqual(file_exist, True)

    def test_session(self):
        current_session = Session(self._user)
        self.assertEqual(current_session.get_current_user(), self._user)

    def test_error_get_user_from_file(self):
        user_manager = UserManager(self._filename)
        with self.assertRaises(ValueError):
            user_manager.get_user_from_file()





if __name__ == '__main__':
    unittest.main()
