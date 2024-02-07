import os.path
import unittest
import uuid

from account import Account
from session import Session
from transaction import Transaction
from user import User
from filemanager import FileManager
from usermanager import UserManager


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._user = User(uuid.uuid4(), 'joe', '7D2d69881*', [], [], 'admin')
        self._user_2 = User(uuid.uuid4(), 'jack', '7D2d69881*', [], [], 'user')
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

    def test_add_account_success(self):
        account_1 = Account(uuid.uuid4(), 2000, self._user)
        self._user.add_account(account_1)
        excepted_list_of_accounts = [account_1]
        self.assertEqual(self._user.get_accounts(), excepted_list_of_accounts)

    def test_transaction_success(self):
        account_1 = Account(str(uuid.uuid4()), 2000, self._user.get_user_id())
        account_2 = Account(str(uuid.uuid4()), 2000, self._user_2.get_user_id())
        self._user.add_account(account_1)
        self._user_2.add_account(account_2)
        transaction = Transaction(str(uuid.uuid4()), account_1, account_2, 50)
        self._user.make_payment(transaction)
        self._user_2.receive_payment(transaction)
        self.assertEqual(account_1.get_amount(), 1950)

if __name__ == '__main__':
    unittest.main()
