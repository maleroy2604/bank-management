class Transaction:
    def __init__(self, transaction_id, account_sender, account_receiver, amount):
        self._id = transaction_id
        self._account_sender = account_sender
        self._account_receiver = account_receiver
        self._amount = amount

    def get_account_sender(self):
        return self._account_sender

    def get_account_receiver(self):
        return self._account_receiver

    def get_amount(self):
        return self._amount
