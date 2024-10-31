import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamahetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus_muutos):
        self.tamahetkinen_nopeus += nopeus_muutos
        if self.tamahetkinen_nopeus > self.huippunopeus:
            self.tamahetkinen_nopeus = self.huippunopeus
        elif self.tamahetkinen_nopeus < 0:
            self.tamahetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamahetkinen_nopeus * tuntimaara

    def print_auto_data(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.tamahetkinen_nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km")

    def print_auto_nopeus(self):
        print(f"Nopeus: {self.tamahetkinen_nopeus} km/h")

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    polttomoottoriauto.kiihdyta(100)

    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print("\nAutojen tiedot kolmen tunnin ajon jälkeen:")
    sahkoauto.print_auto_data()
    polttomoottoriauto.print_auto_data()

main()
