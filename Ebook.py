from Ksiazka import Ksiazka


class Ebook(Ksiazka):
    def __init__(self, tytul: str, autor: str, rok_wydania: int, rozmiar_pliku: float):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self) -> str:
        return f"{super().opis()} - {self.rozmiar_pliku}"