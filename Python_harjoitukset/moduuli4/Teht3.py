import sys
from idlelib.configdialog import is_int
# Ensimmäinen luvun kysely tapahtuu while-loopin ulkopuolella koska on pakko laita joku arvo pieni ja iso muutujen
# sisälle ja jos ma laitan esim. 0 ja käyttäjä myöhemmin ei laita jotain pienempä numeroa, ohjelma
# tulosta lopuksi, että 0 olisi pienin luku vaikka käyttäjä ei laittanut 0 ollenkaan ohjelmaan.
luku = input("Anna luku: ")
# Koska mä en alua, että tulisi error jos käyttäjä laita tyhjän merkkijonon tähän, täytyy käyttää sys.exit() koska
# ei saa käyttä break while-loopin ulkopuolella.
if luku == "":
    print("Ohjelma päättyy.")
    sys.exit()
# Käytän float, koska se antaa käyttäjälle enemmän vapautta numeroiden syöttämisessä ja tehtävä ei pyydä int:tä erikseen.
pieni = iso = float(luku)
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    if float(luku) < float(pieni):
        pieni = luku
    elif float(luku) > float(iso):
        iso = luku
# Jos suurin ja pienin luku ovat int sitten en halua, että olisi joku desimaali vastauksen lopussa a.la 120.0
# Sen takia muutettaan pieni ja iso int:ksi koska sitten vastaus näyttää paremmalta.
if is_int(pieni) and is_int(iso):
    print(f"Pienin luku on {int(pieni)} ja suurin luku on {int(iso)}")
else:
    print(f"Pienin luku on {pieni} ja suurin luku on {iso}")
