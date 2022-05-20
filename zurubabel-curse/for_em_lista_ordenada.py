# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# valor_procurado = 8

# print(f"_o valor procurado é: {valor_procurado}")

# metade_lista = int(len(lista)/2)

# print(f"_a metade é {metade_lista}")

if metade_lista < valor_procurado:
    # print(f"_o valor {valor_procurado} é maior ele está a direita")
    for i in range(metade_lista, len(lista)):
        # print(i)
        if lista[i] == valor_procurado:
            print(f"_o valor {valor_procurado} está na nossa lista")
            break

elif metade_lista > valor_procurado:
    # print(f"_o valor {valor_procurado} é menor ele está a esquerda")
    for i in range(1, len(lista)):
        # print(i)
        if lista[i] == valor_procurado:
            print(f"_o valor {valor_procurado} está na nossa lista")
            break

else:
    print(f"_o valor {valor_procurado} está na nossa lista")
