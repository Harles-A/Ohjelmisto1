import math
# TODO: First ask how many pizzas and then price and size of each and add them to lists.
#  Each time store the cheapest one in the value of cheapest_pizza. At the end say which pizza is cheapest.
def calculate_price(diameter, price):
    #pizzan pinta-ala pi *r^2
    diameter = diameter / 100
    r = diameter / 2
    area = math.pi * r**2

    return price/area

pizza1_diameter = float(input("Syötä 1. pizzan halkaisija senttimetreinä: "))
pizza2_diameter = float(input("Syötä 2. pizzan halkaisija sentti metreinä: "))
pizza1_hinta = float(input("Anna 1. pizzan hinta: "))
pizza2_hinta = float(input("Anna 2. pizzan hinta: "))

pizza1_nelio_hinta = calculate_price(pizza1_diameter, pizza1_hinta)
pizza2_nelio_hinta = calculate_price(pizza2_diameter, pizza2_hinta)

print(f"Ensimmäisen pizzan hinta on {pizza1_nelio_hinta:.2f}.")
print(f"Toisen pizzan hinta on {pizza2_nelio_hinta:.2f}.")

if pizza1_nelio_hinta < pizza2_nelio_hinta:
    print("Ensimmäinen pizza on halvempi")
elif pizza2_nelio_hinta > pizza1_nelio_hinta:
    print("Toinen pizza on halvempi")
else:
    print("Pizzojen neliöhinta on sama.")
