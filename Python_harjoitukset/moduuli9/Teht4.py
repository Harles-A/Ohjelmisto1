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


def main():
    cars = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        cars.append(Auto(rekisteritunnus, huippunopeus))

    tunnit = 0

    while True:
        tunnit += 1
        for i in cars:
            muutos = random.randint(-10, 15)
            i.kiihdyta(muutos)
            i.kulje(1)

            if i.kuljettu_matka >= 10000:
                break
        else:
            continue
        break

    for i in cars:
        i.print_auto_data()


main()
