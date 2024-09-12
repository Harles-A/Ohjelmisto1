
lentoasemat = {}

def lisa_asema():
    icao_lisa = input("Anna lentoaseman ICAO-koodi: ")
    icao_lisa = icao_lisa.upper()
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[icao_lisa] = nimi

def etsi_asema():
    icao_etsi = input("Anna ICAO-koodi: ")
    icao_etsi = icao_etsi.upper()
    if icao_etsi in lentoasemat:
        print(f"Lentoaseman {icao_etsi} nimi on: {lentoasemat[icao_etsi]}")
    else:
        print(f"{icao_etsi} koodilla ei löydy lentoasemaa.")

# Pääohjelma
while True:
    print("1. Lisä uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")
    valinta = input("Valitse toiminto numerolla: ")

    if valinta == "1":
        lisa_asema()
    elif valinta == "2":
        etsi_asema()
    elif valinta == "3":
        print("Ohjelma lopeta")
        break
