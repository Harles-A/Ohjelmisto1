vuosi = int(input("Anna vuosiluku: "))

if vuosi % 100 == 0 and vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 != 0:
    print(f"{vuosi} ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print(f"{vuosi} on karkausvuosi.")
elif vuosi % 4 != 0:
    print(f"{vuosi} ei ole karkausvuosi.")
else:
    print("Error. x.x ")