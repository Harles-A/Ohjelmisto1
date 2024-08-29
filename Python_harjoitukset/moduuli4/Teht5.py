kayttajatunnus = "python"
salasana = "rules"
vaari = 0
while vaari < 5:
    vastaus1 = input("Anna käyttäjätunnus: ")
    vastaus2 = input("Anna salasana: ")
    if vastaus1 == kayttajatunnus and vastaus2 == salasana:
        print("Tervetuloa")
        break
    else:
        vaari += 1
    if vaari == 5:
        print("Pääsy evätty")



