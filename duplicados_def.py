lista1 = [1, 6, 3, 4, 5]


def tem_duplicados(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

# O(N^2)


print(tem_duplicados(lista1))
