from random import randint

def noppa_heitto():
    return randint(1, 6)

while True:
    tulos = noppa_heitto()
    print(f"Nopan tulos on: {tulos}")
    if tulos == 6:
        break
    else:
        continue

