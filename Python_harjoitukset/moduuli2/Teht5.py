leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luodi = float(input("Anna luodit: "))

naula = naula + (leiviska * 20)
luodi = luodi + (naula * 32)
gramma = luodi * 13.3

kilos = gramma // 1000
ylijaama = gramma % 1000

print(f"Massa nykymittojen mukaan: {int(kilos)} kilogramma ja {ylijaama:.2f} gramma.")