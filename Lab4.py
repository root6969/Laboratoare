from Lab3 import Film # type: ignore
class FilmDocumentar(Film):
    def __init__(self, nr=0, denumire="", gen="", regizor="", durata=0, tara="", domeniu="", elemente_artistice=False):
        super().__init__(nr, denumire, gen, regizor, durata, tara)
        self.domeniu = domeniu
        self.elemente_artistice = elemente_artistice

    @classmethod
    def cu_toti_parametrii(cls, nr, denumire, gen, regizor, durata, tara, domeniu, elemente_artistice):
        return cls(nr, denumire, gen, regizor, durata, tara, domeniu, elemente_artistice)

    @classmethod
    def cu_unii_parametrii(cls, nr, denumire, gen, domeniu):
        return cls(nr, denumire, gen, "Necunoscut", 120, "Necunoscut", domeniu, False)

    def seteaza_domeniu(self, domeniu):
        self.domeniu = domeniu

    def seteaza_elemente_artistice(self, elemente_artistice):
        self.elemente_artistice = elemente_artistice

    def afisare(self):
        super().afisare()
        print(f"Domeniu: {self.domeniu}")
        print(f"Elemente artistice: {'Da' if self.elemente_artistice else 'Nu'}")

class FilmShow(FilmDocumentar):
    def __init__(self, nr=0, denumire="", gen="", regizor="", durata=0, tara="", domeniu="", elemente_artistice=False, tema="", actori=[]):
        super().__init__(nr, denumire, gen, regizor, durata, tara, domeniu, elemente_artistice)
        self.tema = tema
        self.actori = actori

    @classmethod
    def cu_toti_parametrii(cls, nr, denumire, gen, regizor, durata, tara, domeniu, elemente_artistice, tema, actori):
        return cls(nr, denumire, gen, regizor, durata, tara, domeniu, elemente_artistice, tema, actori)

    @classmethod
    def cu_unii_parametrii(cls, nr, denumire, gen, domeniu, tema):
        return cls(nr, denumire, gen, "Necunoscut", 120, "Necunoscut", domeniu, False, tema, [])

    def seteaza_tema(self, tema):
        self.tema = tema

    def seteaza_actori(self, actori):
        self.actori = actori

    def afisare(self):
        super().afisare()
        print(f"Tema: {self.tema}")
        print(f"Actori: {', '.join(self.actori)}")

# Exemplu de utilizare
film1 = Film()
film2 = Film.cu_toti_parametrii(1, "Inception", "Sci-Fi", "Christopher Nolan", 148, "USA")
film3 = FilmDocumentar.cu_toti_parametrii(2, "Planet Earth", "Documentar", "David Attenborough", 60, "UK", "Natură", True)
film4 = FilmShow.cu_toti_parametrii(3, "The Tonight Show", "Talk Show", "Jimmy Fallon", 60, "USA", "Divertisment", False, "Comedie", ["Jimmy Fallon", "Invitați"])

film1.afisare()
print()
film2.afisare()
print()
film3.afisare()
print()
film4.afisare()