from zajecia2.zadanie2.UserNotFoundError import UserNotFoundError
from zajecia2.zadanie2.WrongPasswordError import WrongPasswordError


class UserAuth:
    def __init__(self, users: dict):
        self.users = users

    def login(self, username: str, password: str):
        """Sprawdza, czy podane dane logowania są poprawne."""
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik '{username}' nie istnieje.")

        if self.users[username] != password:
            raise WrongPasswordError("Niepoprawne hasło.")

        print(f"Zalogowano pomyślnie jako '{username}'.")
