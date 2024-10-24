class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamahetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamahetkinen_nopeus = tamahetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

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


def main():
    auto1 = Auto("ABC-123", 142, tamahetkinen_nopeus = 60, kuljettu_matka = 2000)
    auto1.kulje(1.5)
    auto1.print_auto_data()

main()
