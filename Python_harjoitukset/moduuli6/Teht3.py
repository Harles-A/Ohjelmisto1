
def gall_to_litra(gall_arvo):
    return gall_arvo * 3.785

gall_input = 0
while True:
    gall_input = float(input("Anna bensiinin määrä nestegallonoina: "))
    if gall_input < 0:
        print("Annetu määrä on negatiivinen. Ohjelma lopeta.")
        break
    litra_output = gall_to_litra(gall_input)
    print(f"{gall_input} nestegallona on {litra_output:.3f} litra")

