class Kissa:
    def __init__(self, nimi, age):
        self.nimi = nimi
        self.ika = age
        self.omistaja = "Tuntematon"


ekaKissa = Kissa("Kitty", 5)

print(f"Kissan nimi on {ekaKissa.nimi}")
