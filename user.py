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
