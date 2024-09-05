
from random import randint

kuutiot = int(input("Kuinka monta arpakuutiota?: "))
summa = 0
for i in range(kuutiot):
    kuutio_tulos = randint(1,6)
    summa += kuutio_tulos

print(f"Arpakuutioiden silmälukujen summa on {summa}.")