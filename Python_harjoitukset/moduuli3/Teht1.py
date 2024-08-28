kuha = float(input("Mikä on kuhan pituus senttimetreinä? "))

if kuha < 37.0:
    print(f"Kuha on {37.0 - kuha} senttiä alimmasta sallitusta pyyntimitasta lyhyempi. Laske kuha takaisin järve.")
elif kuha > 37.0:
    print(f"Kuha on {kuha - 37.0} senttiä alimmasta sallitusta pyyntimitasta pitempi. Hyvä!")
else:
    print("Error x.x ")