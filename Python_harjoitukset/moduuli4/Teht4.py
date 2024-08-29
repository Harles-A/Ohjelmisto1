import random

luku = random.randint(1, 10)
vastaus = 0
while vastaus != luku:
    vastaus = int(input("Anna kokonaisluku 1 ja 10 väliltä: "))
    if vastaus < luku:
        print("Liian pieni arvaus")
    elif vastaus > luku:
        print("Liian suuri arvaus")
    elif vastaus == luku:
        print("Oikea arvaus")