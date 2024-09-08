
def parittomat_pois(lista):
    return [numero for numero in lista if numero % 2 == 0]

lista = [1, 3, 4, 6, 7, 11, 19, 20, 23, 40, 100]
parilisset_lista = parittomat_pois(lista)

print(f"Alkuperäinen lista oli: {lista}")
print(f"Karsitu lista on: {parilisset_lista}")