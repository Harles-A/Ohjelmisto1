maara = 0
while maara >= 0:
    maara = float(input("Anna tuumien määrä: "))
    if maara >= 0:
        print(f"{maara} tuuma on {maara * 2.54} senttimetria.")
    else:
        print("Ohjelma lopettaa.")