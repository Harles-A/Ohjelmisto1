# Tein tämä tehtävän kahdella eri tavalla. Tässä on ensimmäinen ja alhalla on viellä toinen comment-block:in sisällä. ( Rivit 24-44 )
# Tehtään monikkotietorakente vuodenaj...oista?...aikoista? No that doesn't sound right. Let's go with vuodenajoista!
vuodenajat = (
    ("Kevät", [3, 4, 5]),
    ("Kesä", [6, 7, 8]),
    ("Syksy", [9, 10, 11]),
    ("Talvi", [12, 1, 2])
)

kausinumero = int(input("Anna kuukauden numero: "))

# Katsotaan mikä kuukausi se on mitkä vastaa annetuun numeroon
for vuodenaika, kuukaudet in vuodenajat:
    if kausinumero in kuukaudet:
        print(f"Kuukaudelle {kausinumero} vastaavan vuodenaika on {vuodenaika}.")
        break
# Jos käyttäjä anna väärän numeron, esim. 20, sanotaan hänelle, että pitää käyttää numeroa väliltä 1-12.
# Jos hän anna esimerkiksi stringin, ei numeron, ohjelma kaatuu anyway.
else:
    print("Väärä numero. Anna numero väliltä 1-12.")


'''
vuodenajat = ("Kevät","Kesä","Syksy","Talvi")

def vuodenaika(kausinumero):
    if kausinumero in [3, 4, 5]:
        return vuodenajat[0]
    elif kausinumero in [6, 7, 8]:
        return vuodenajat[1]
    elif kausinumero in [9, 10, 11]:
        return vuodenajat[2]
    elif kausinumero in [12, 1, 2]:
        return vuodenajat[3]
    else:
        return None

kausinumero = int(input("Anna kuukauden numero: "))
vastaus = vuodenaika(kausinumero)

if vastaus:
    print(f"Kuukaudelle {kausinumero} vastaavan vuodenaika on {vastaus}.")
else:
    print("Väärä numero. Anna numero väliltä 1-12.")
'''
