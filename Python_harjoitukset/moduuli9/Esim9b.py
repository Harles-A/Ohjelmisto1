class Kissa:

   kissojenLkm = 0

   def __init__(self, nimi, age, tervehdys = "Miau, miau!"):
        self.nimi = nimi
        self.ika = age
        self.omistaja = "Tuntematon"
        self.tervehdys = tervehdys
        Kissa.kissojenLkm += 1

   def tetvehdi(self):
        print(self.tervehdys)


tokaKissa = Kissa("Mörri", 3, tervehdys = "Mrraawr!")
kolmasKissa = Kissa("Mirri", 1)

tokaKissa.tetvehdi()
kolmasKissa.tetvehdi()
print(f"Kissa-olioita on luotu {Kissa.kissojenLkm}")