class Kissa:

   kissojenLkm = 0

   def __init__(self, nimi, age, tervehdys = "Miau, miau!", omistaja=None):
        self.nimi = nimi
        self.ika = age
        self.omistaja = omistaja
        omistaja.lisaa_kissa(self)
        self.tervehdys = tervehdys
        Kissa.kissojenLkm += 1

   def tervehdi(self):
        print(f"{self.tervehdys}! olen {self.nimi}")
        print(f"Ikäni on {self.ika}")
        print(f"Omistajani on {self.omistaja.nimi}")


class Omistaja:
    def __init__(self, nimi, puh="Tuntematon"):
        self.nimi = nimi
        self.puh = puh
        self.cats = []

    def lisaa_kissa(self, kissa):
        for k in self.cats:
            if k == kissa:
                return
        self.cats.append(kissa)

    def esittele(self):
        print(f"Olen {self.nimi}, puh: {self.puh}")
        print(f"Omistan kissat: ")
        for cat in self.cats:
            print(f"{cat.nimi}, ika: {cat.ika}")


viivi = Omistaja("Viivi Virtanen")

cat1 = Kissa("Mörri", 3, "Mrraawr!", viivi)
cat2 = Kissa("Mirri", 1, omistaja=viivi)


cat1.tervehdi()
cat2.tervehdi()
#viivi.lisaa_kissa(cat1)
#viivi.lisaa_kissa(cat1)
#viivi.lisaa_kissa(cat2)
viivi.esittele()

for kissa in viivi.cats:
    kissa.tervehdi()

"""
cats = []
for i in range(5):
    new_cat = Kissa(f"Cat name {1}", i+2, f"Moro {i+1}")
    cats.append(new_cat)
for i in cats:
    i.tervehdi()
"""
print(f"---\nKissa-olioita on luotu {Kissa.kissojenLkm}")
