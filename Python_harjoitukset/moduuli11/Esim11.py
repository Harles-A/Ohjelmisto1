class Koira():
    def __init__(self, nimi, tervehdys="Hau hau!"):
        self.nimi = nimi
        self.tervehdys = tervehdys

    def tervehdi(self):
        print(self.tervehdys)


class RotuKoira(Koira):
    def __init__(self, nimi, rotu, tervehdys="Hau hau!"):
        super().__init__(nimi, tervehdys)
        self.rotu = rotu

    def tervehdi(self):
        print(f"{self.tervehdys}, rotuni on {self.rotu}.")


koiraA = Koira("Ressu")
hieno_koira = RotuKoira("Mr. Bean", "beagle", tervehdys="Vuh, vuh!")
koiraA.tervehdi()
hieno_koira.tervehdi()