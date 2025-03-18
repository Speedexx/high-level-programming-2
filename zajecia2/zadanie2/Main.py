from zajecia2.zadanie2.UserAuth import UserAuth
from zajecia2.zadanie2.UserNotFoundError import UserNotFoundError
from zajecia2.zadanie2.WrongPasswordError import WrongPasswordError

if __name__ == "__main__":
    auth = UserAuth({"admin": "1234", "user": "abcd"})

    try:
        auth.login("admin", "1234")  # Sukces
    except Exception as e:
        print(f"Błąd: {e}")

    try:
        auth.login("unknown", "pass")  # Powinien rzucić UserNotFoundError
    except UserNotFoundError as e:
        print(f"Błąd: {e}")

    try:
        auth.login("user", "wrongpass")  # Powinien rzucić WrongPasswordError
    except WrongPasswordError as e:
        print(f"Błąd: {e}")
