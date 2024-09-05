from random import randint

tahku = int(input("Kuinka monta tahkua?: "))

def noppa_heitto(tahku):
    return randint(1, tahku)

while True:
    tulos = noppa_heitto(tahku)
    print(f"Nopan tulos on: {tulos}")
    if tulos == tahku:
        break
    else:
        continue