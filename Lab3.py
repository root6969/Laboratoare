class Film:
    def __init__(self, nr=0, denumire="", gen="", regizor="", durata=0, tara=""):
        self.nr = nr
        self.denumire = denumire
        self.gen = gen
        self.regizor = regizor
        self.durata = durata
        self.tara = tara

    # Constructor cu toți parametrii
    @classmethod
    def cu_toti_parametrii(cls, nr, denumire, gen, regizor, durata, tara):
        return cls(nr, denumire, gen, regizor, durata, tara)

    # Constructor cu unii parametrii
    @classmethod
    def cu_unii_parametrii(cls, nr, denumire, gen):
        return cls(nr, denumire, gen, "Necunoscut", 120, "Necunoscut")

    # Setters
    def seteaza_nr(self, nr):
        self.nr = nr

    def seteaza_denumire(self, denumire):
        self.denumire = denumire

    def seteaza_gen(self, gen):
        self.gen = gen

    def seteaza_regizor(self, regizor):
        self.regizor = regizor

    def seteaza_durata(self, durata):
        self.durata = durata

    def seteaza_tara(self, tara):
        self.tara = tara

    # Getters
    def get_nr(self):
        return self.nr

    def get_denumire(self):
        return self.denumire

    def get_gen(self):
        return self.gen

    def get_regizor(self):
        return self.regizor

    def get_durata(self):
        return self.durata

    def get_tara(self):
        return self.tara

    # Metoda de calcul a duratei în ore
    def durata_in_ore(self):
        return round(self.durata / 60, 1)

    # Metoda de afișare a informațiilor despre film
    def afisare(self):
        print(f"Nr: {self.nr}")
        print(f"Denumire: {self.denumire}")
        print(f"Gen: {self.gen}")
        print(f"Regizor: {self.regizor}")
        print(f"Durata: {self.durata} minute")
        print(f"Țara: {self.tara}")

# Exemplu de utilizare
film1 = Film()
film2 = Film.cu_toti_parametrii(1, "Inception", "Sci-Fi", "Christopher Nolan", 148, "USA")
film3 = Film.cu_unii_parametrii(2, "Avatar", "Fantasy")

film1.afisare()
print()
film2.afisare()
print()
film3.afisare()
print("-------------------------------------")
print(f"Durata filmului {film2.denumire} în ore: {film2.durata_in_ore()}")
print("-------------------------------------")