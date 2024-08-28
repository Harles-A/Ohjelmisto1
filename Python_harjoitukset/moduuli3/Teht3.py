spuoli = input("Anna biologinen sukupuoli (m/n): ")
hemogoblin = float(input("Anna hemoglobiiniarvo: "))

if spuoli == "n" and 117 <= hemogoblin <= 175:
    print("Hemoglobiiniarvo on normaali.")
elif spuoli == "n" and hemogoblin > 175:
    print("Hemoglobiiniarvo on korkea.")
elif spuoli == "n" and hemogoblin < 117:
    print("Hemoglobiiniarvo on alhainen.")
elif spuoli == "m" and 134 <= hemogoblin <= 195:
    print("Hemoglobiiniarvo on normaali.")
elif spuoli == "m" and hemogoblin > 195:
    print("Hemoglobiiniarvo on korkea.")
elif spuoli == "m" and hemogoblin < 134:
    print("Hemoglobiiniarvo on alhainen.")
else:
    print("Error! x.x ")
