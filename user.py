class User:
    def __init__(self, user_id, name, password, accounts, transactions, role):
        self._id = user_id
        self._name = name
        self._password = password
        self._accounts = accounts
        self._transactions = transactions
        self._role = role

    def __eq__(self, other):
        if isinstance(other, User):
            return (
                    self._id == other._id and
                    self._name == other._name and
                    self._password == other._password and
                    self._accounts == other._accounts and
                    self._role == other._role
            )
        return False

    def get_role(self):
        return self._role

    def get_user_id(self):
        return self._id

    def get_accounts(self):
        return self._accounts

    def add_account(self, account):
        self._accounts.append(account)

    def find_account(self, account_id):
        for account in self._accounts:
            if account.get_account_id() == account_id:
                return account
            else:
                raise ValueError(f"account n° {account_id} not found")

    def make_payment(self, transaction):
        account_id = transaction.get_account_sender().get_account_id()
        account = self.find_account(account_id)
        account.withdraw(transaction.get_amount())

    def receive_payment(self, transaction):
        account_id = transaction.get_account_receiver().get_account_id()
        account = self.find_account(account_id)
        account.deposit(transaction.get_amount())
        








