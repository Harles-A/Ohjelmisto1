nimet = []

lkm = int(input("Kuinka monta osallistujaa?: "))

for i in range(lkm):
    nimi = input("Anna nimi: ")
    #lisätään nimet listaan loppuun
    nimet.append(nimi)

#järjestetään nimet aakkosjärjestykseen
nimet.sort()

print("Nimet aakkosjärjestyksessä: ")
print(nimet)

#muokataan listan alkioiden sisältöja
nimet[1] = "Toka" #huom indeksin numero
nimet[-1] = "Vika"
nimet.insert(0,"Uusi eka")
#tulostetaan listan alkiot kukin omalla rivillään (for .. in)
for alkio in nimet:
    print(alkio)