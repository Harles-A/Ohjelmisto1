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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeus_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeus_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailun '{self.nimi}' tilanne:")
        for auto in self.autot:
            auto.print_auto_data()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

def main():
    cars = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        cars.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu = Kilpailu("Suuri Romuralli", 8000, cars)
    tunnit = 0

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    print("\nKilpailu Päätynyt!")
    kilpailu.tulosta_tilanne()

main()
