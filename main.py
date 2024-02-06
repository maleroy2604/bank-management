from session import Session
from usermanager import UserManager
from user import User
import uuid


class Main:

    def start_bank(self):
        user_1 = User(str(uuid.uuid4()), 'joe', '7D2d69881*', [], [], 'admin')
        user_2 = User(str(uuid.uuid4()), 'jack', '7D2d69881*', [], [], 'normal')
        current_session = Session(user_1)
        if current_session.get_current_user().get_role() == 'admin':
            user_manager = UserManager('users.txt')
            user_manager.add_user(user_1)
            user_manager.add_user(user_2)
        else:
            raise ValueError("You do not have access to those functionalities")

        print(user_manager.get_user_from_file())


if __name__ == '__main__':
    main = Main()
    main.start_bank()
