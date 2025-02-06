from abc import ABC, abstractmethod

class Depozit(ABC):
    def __init__(self, suma_initiala, rata):
        self.suma_initiala = suma_initiala
        self.rata = rata

    @abstractmethod
    def sumaFinala(self):
        pass

class Depozit12Luni(Depozit):
    def __init__(self, suma_initiala, rata):
        super().__init__(suma_initiala, rata)

    def sumaFinala(self):
        return self.suma_initiala * (1 + self.rata / 100) ** 1  # 12 luni = 1 an

class Depozit6Luni(Depozit):
    def __init__(self, suma_initiala, rata):
        super().__init__(suma_initiala, rata)

    def sumaFinala(self):
        return self.suma_initiala * (1 + self.rata / 100 / 2) ** 1  # 6 luni = 0.5 ani

# Exemplu de utilizare și polimorfism
def afiseaza_suma_finala(depozit, tip_depozit):
    print(f"Suma finală pentru depozit {tip_depozit}: {depozit.sumaFinala()}")

depozit_12_luni = Depozit12Luni(1000, 5)  # 1000 unități monetare, 5% rată
depozit_6_luni = Depozit6Luni(1000, 5)    # 1000 unități monetare, 5% rată

afiseaza_suma_finala(depozit_12_luni, "12 luni")
afiseaza_suma_finala(depozit_6_luni, "6 luni")