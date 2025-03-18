class Ksiazka:
    def __init__(self, tytul: str, autor: str, rok_wydania: int):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self) -> str:
        return f"{self.tytul} - {self.autor} ({self.rok_wydania})"