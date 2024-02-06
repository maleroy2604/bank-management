class Session:
    def __init__(self, user):
        self._current_user = user

    def get_current_user(self):
        return self._current_user
