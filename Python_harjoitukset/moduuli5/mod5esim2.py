print("Tulostan parilliset luvut väliltä 10 ... 20")

for nro in range(10,21,2): #10 kuuluu tarkasteltavaan välin, 21 ei kuulu. Kolmas parametri kertoo lisäyksen määrän.
    print(nro)

print("Tulostetaan kaikki luvut väliltä 5 ... 10")

for nro in range(5,11): print(nro)

for nro in range(5):
    print(f"Hei {nro + 1}. kerran")