from Audiobook import Audiobook
from Ebook import Ebook
from Ksiazka import Ksiazka


def main():
    # Testowanie klas
    ksiazka = Ksiazka("Wiedźmin", "Andrzej Sapkowski", 1993)
    ebook = Ebook("Wiedźmin", "Andrzej Sapkowski", 1993, 5.2)
    audiobook = Audiobook("Wiedźmin", "Andrzej Sapkowski", 1993, 720)

    print(ksiazka.opis())
    print(ebook.opis())
    print(audiobook.opis())

if __name__ == "__main__":
    main()