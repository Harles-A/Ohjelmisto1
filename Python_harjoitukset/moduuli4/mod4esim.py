import random



command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "lopeta":
        print("Lopetetaan ohjelma")
    elif command == "hurraa":
        hurraa_arvo = int(input("Kuinka monta kertaa hurrataan? "))
        hurraa_laskin = 0
        while hurraa_laskin < hurraa_arvo:
            hurraa_laskin += 1 # hurraa_laskin = hurraa_laskin +1
            print(f"{hurraa_laskin}. kerran Hurraa!")
        print(f"Hurrattiin {hurraa_laskin} kerta.")
    elif command == "noppa":
        test_count = 0
        total_throw_count = 0
        while test_count < 100000:
            test_count += 1
            die1 = 0
            die2 = 0
            counter = 0
            while die1 != 6 or die2 != 6:
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                counter += 1
                # print(f"Noppien silmäluvut: {die1}, {die2}, heittojen määrä: {counter}")
            total_throw_count += counter
            #print(f"Heittojen määrä tällä kierroksella: {counter}, yhteensä: {total_throw_count}")
        print(f"Heittojen lukumäärä keskiarvo: {total_throw_count / test_count}")
    elif command == "silmukka":
        eka = 1
        while eka <= 5:
            print("Ulompi silmukka alkaa")
            toka = 1
            while toka <= 5:
                print("Sisempi silmukka alkaa")
                print(f"{eka} kertaa {toka} on {eka * toka:d}")
                toka = toka + 1
            eka = eka + 1
    else:
        print("En ymmärrä. Tarkista komentosi, kiitos.")
print("Ohjelman suoritus loppui.")

