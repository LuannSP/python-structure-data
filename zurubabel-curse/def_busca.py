def busca(lista, elem):  # O(n)
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


"""
lista = [1, 3, 54, 6, 7, 8, 19]
elem = 19

idx = busca(lista, elem)

if idx is not None:
    print(f"O index do elemento {elem} é {idx}")
else:
    print(f"O elemento {elem} não está na nossa lista!")
"""
