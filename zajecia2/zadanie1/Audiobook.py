from Ksiazka import Ksiazka


class Audiobook(Ksiazka):
    def __init__(self, tytul: str, autor: str, rok_wydania: int, czas_trwania: float):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self) -> str:
        return f"{super().opis()} - {self.czas_trwania}"