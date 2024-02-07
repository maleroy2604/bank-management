from session import Session
from transaction import Transaction
from usermanager import UserManager
from user import User
from account import Account
import uuid


class Main:

    def start_bank(self):

        user_1 = User(str(uuid.uuid4()), 'joe', '7D2d69881*', [], [], 'admin')
        user_2 = User(str(uuid.uuid4()), 'jack', '7D2d69881*', [], [], 'normal')
        account_1 = Account(str(uuid.uuid4()), 2000, user_2.get_user_id())
        account_2 = Account(str(uuid.uuid4()), 1500, user_1.get_user_id())
        transaction = Transaction(str(uuid.uuid4()), account_1, account_2, 500)
        current_session = Session(user_1)
        if current_session.get_current_user().get_role() == 'admin':
            user_manager = UserManager('users.txt')
            user_2.add_account(account_2)
            user_1.add_account(account_1)
            user_1.make_payment(transaction)
            user_2.receive_payment(transaction)
            print(account_1.get_amount())
            print(account_2.get_amount())
            user_manager.add_user(user_1)
            user_manager.add_user(user_2)
        else:
            raise ValueError("You do not have access to those functionalities")

        print(user_manager.get_user_from_file())


if __name__ == '__main__':
    main = Main()
    main.start_bank()
