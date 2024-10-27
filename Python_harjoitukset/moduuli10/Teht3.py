class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros
    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()
    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin:
            return
        else:
            self.nykyinen_kerros += 1
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")
    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin:
            return
        else:
            self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.hissit = []
        self.luo_hissit(lkm)

    def luo_hissit(self, lkm):
        for nro in range(lkm):
            uusi_hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(uusi_hissi)
        return

    def aja_hissiä(self, hissin_nro, kohdekerros):
        ajettava_hissi = self.hissit[hissin_nro - 1]
        ajettava_hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)



taloesim = Talo(1, 8, 2)
taloesim.aja_hissiä(1, 6)
taloesim.aja_hissiä(1, 3)
taloesim.aja_hissiä(2, 4)
taloesim.palohalytys()
