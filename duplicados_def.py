def tem_duplicados(lista):  # O(N^2)
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            print(f"{lista[i]} é igual a {lista[j]}")
            if lista[i] == lista[j]:
                return True
    return False
