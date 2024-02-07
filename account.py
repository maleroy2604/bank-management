class Account:
    def __init__(self, account_id, amount, user_id):
        self._id = account_id
        self._amount = amount
        self._user_id = user_id

    def set_amount(self, amount):
        self._amount = amount

    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_amount(self):
        return self._amount

    def get_user_id(self):
        return self._user_id

    def get_account_id(self):
        return self._id

    def withdraw(self, amount):
        self._amount -= amount

    def deposit(self, amount):
        self._amount += amount
