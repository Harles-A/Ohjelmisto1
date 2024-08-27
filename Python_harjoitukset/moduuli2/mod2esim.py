import math

# Kysytään käyttäjältä syöte (input)
# Ja sijoitetaan käyttäjä syöttämä merkkijono (string) muuttujaan
name = input("Anna nimesi: ")
# Tulostetaan muuttujan arvo (output)
print("Moi " + name)
# Tallennetaan ikä kokonaislukuna (int)
age = int(input("Anna ikä: "))
print(age)
print("Moi " + name + " ikäsi on " + str(age))
# Lisätään ikään 1 vuosi
age = age +1
print(f"Vuoden päästä ikäsi on {age:6.2f}")

print(f"Piin likiarvo: {math.pi:.2f}")

# t2
r = float(input("Anna ympyrän säde: "))
area = math.pi * r**2 # math.pi * r * r
area = round(area, 2) # pyöristys 2 desimaalin tarkkuuteen
print(f"Ympyrän pinta-ala on {area:.2f} neliömetriä.")
