
luku_lista = []
# While-loop on parempi tässä paikassa (imho) mutta koska se on for-loop tehtävä luulin, että täytyy käyttää for-loop.
# Alhalla (lines 38 - 44) on myös while-loop versio tästä loopista.
for i in range(10**100):
    luku = input("Anna luku: ")
    if luku == "":
        break
    else:
        # Tehtävässä ei ole kirjoitettu, että pitää käyttää int, käytän float koska why not. 120.5 on myös luku.
        luku = float(luku)
    luku_lista.append(luku)

luku_lista.sort(reverse=True)

# Alussa minulla oli tässä vain:
'''
print("Viisi suurimmat luku ovat: ")
for i in range(5):
    print(luku_lista[i])
'''
# mutta jos käyttäjä syötä vähemmän kuin 5 luku, se anna errorin, sen takia
# lisäsin vaihtoehton jos on vähemämän kuin 5 luku listassa

if len(luku_lista) < 5:
    print(f"{len(luku_lista)} suurimmat luku ovat: ")
elif len(luku_lista) >= 5:
    print("Viisi suurimmat luku ovat: ")

if len(luku_lista) < 5:
    for i in range(len(luku_lista)):
        print(luku_lista[i])
elif len(luku_lista) >= 5:
    for i in range(5):
        print(luku_lista[i])

'''
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    else:
        luku = float(luku)
    luku_lista.append(luku)
'''
