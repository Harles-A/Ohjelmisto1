# Piin likiarvon laskeminen
# n/N≈π/4, jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# x^2+y^2<1 epäyhtälöllä testataan, onko yksittäinen piste ympyrän sisällä
import math
import random
iterator = 0
N = int(input("Anna pisteiden määrä: ")) # Pisteiden kokonaismäärä
n = 0 # Ympyrään sisään osuvat pisteet
while iterator < N:
    # Arvataan koordinaatit liukulukuina väliltä -1 ja 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    iterator += 1
    #print(f"Satunnainen piste: {x}, {y}")
    #print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        #print("Osui ympyrän sisälle")
        n += 1
print(f"{N} pisteestä {n} osui yksikkö ympyrän sisälle")
vastaus = 4 * n / N
print(f"Piin likiarvo on {vastaus}")
#print(f"Virhe: {vastaus - math.pi}")
