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

    def print_auto_data(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.tamahetkinen_nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km")

    def print_auto_nopeus(self):
        print(f"Nopeus: {self.tamahetkinen_nopeus} km/h")


def main():
    auto1 = Auto("ABC-123", 142)
    auto1.print_auto_data()
    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)
    auto1.print_auto_nopeus()
    auto1.kiihdyta(-200)
    auto1.print_auto_nopeus()

main()
