def inverterLista(lista):
    novaLista = []
    tamanho = len(lista)-1
    for i in range(tamanho):
        novaLista.append(lista[tamanho-i])
        if i == (tamanho-1):
            novaLista.append(lista[tamanho-tamanho])
    return novaLista


def inverterLista2(lista):
    newList = [num for num in reversed(lista)]
    return newList


def inverterLista3(lista):
    newList = lista[::-1]
    return newList
