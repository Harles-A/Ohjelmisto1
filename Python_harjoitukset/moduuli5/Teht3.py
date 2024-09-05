
luku = int(input("Anna kokonaisluku: "))
alkuluku = True
# Koska ei voi jakaa 0:lla ja kaikki numerot on jaoliset 1:lla me aloitame for-loopin numerosta 2.
# Koska for-loopin viimainen luku (luku) on exclusionary,
# tämä looppi katso onko luku jaollinen muulla kuin 1 tai itse.
for i in range(2, luku):
    # Jos on sitten me muutamme alkuluku boolean:in False
    if luku % i == 0:
        alkuluku = False
# Jos käyttäjä laita 0 ta 1 input:iin sitten meidän for-loop ei toimi.
# Meidän pitää se eriksen käsitellä for-loopin ulkopuolella.
if luku == 0 or luku == 1:
    alkuluku = False
# Jos alkuluku on viellä True sitten se tarkoita, että luku oli alkuluku.
if alkuluku:
    print(f"{luku} on alkuluku!")
else:
    print(f"{luku} ei ole alkulukuku!")
