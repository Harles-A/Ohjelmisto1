def do_something():
    print("Tämä aliohjelma tekee")
    print("jotain!")
    return "Tämä on funktion palauttama merkkijono"

#return_value = do_something()
#print(return_value)

def say_hello(to):
    #print("Moi " + to)
    return "Moi " + to

#say_hello("Miki")
#print(say_hello("Miki"))

#def create_greeting(to, count):
#    greet_list = []
#    for i in range(1, count+1):
#        greet_list.append(f"{i}. kerran Moi " + to)
#
#    return greet_list

#create_greeting("Miki", 3)

#greetings = create_greeting("Miki", 3)
#print(greetings)
#for i in range(len(greetings)):
#    print(greetings[i])
#for greeting in greetings:
#    print(greeting)
import random

def noppa_game():
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
        # print(f"Heittojen määrä tällä kierroksella: {counter}, yhteensä: {total_throw_count}")
    print(f"Heittojen lukumäärä keskiarvo: {total_throw_count / test_count}")

def hurraa_funktio():
    hurraa_arvo = int(input("Kuinka monta kertaa hurrataan? "))
    hurraa_laskin = 0
    while hurraa_laskin < hurraa_arvo:
        hurraa_laskin += 1  # hurraa_laskin = hurraa_laskin +1
        print(f"{hurraa_laskin}. kerran Hurraa!")
    print(f"Hurrattiin {hurraa_laskin} kerta.")

command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "lopeta":
        print("Lopetetaan ohjelma")
    elif command == "hurraa":
        hurraa_funktio()
    elif command == "noppa":
        noppa_game()
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

main_app_var = 5
def modify_value():
    global main_app_var
    main_app_var = 1
print(main_app_var)

def print_inventory(inventory):
    print("Pelaajalla on: ")
    for item in inventory:
        print(item)

player1_inventory = ["veitsi", "vesipullo"]
player2_inventory = ["kirves", "eväsleipä"]

print_inventory(player2_inventory)

def calc_sum_adv(*nums):
    total = 0
    calculation = "Laskutoimitus: "
    for num in nums:
        total += num
        calculation = calculation + " +" + str(num)
    print(calculation)
    return total

print(calc_sum_adv(1,2,3,6))