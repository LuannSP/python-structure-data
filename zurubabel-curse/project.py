veio = False
tu_e_estudante_sabe_vua = False
gravida = False
desc_multiplicador = 0.9

ticket_cineminha = 19.99
valor_final = ticket_cineminha

print("Hello World!")

print("Soma: " + str(1 + 1))
print("Subtração: " + str(3 - 1))
print("Divisão real: " + str(5 / 5))
print("Divisão int: " + str( 5.5 // 5.5))
print("Modulo (Resto da divisão): " + str(5 % 3))
print("Potenciacão: " + str(5 ** 5))

nmr = 10

print(id(nmr))

nmr = 20

print(id(nmr))

nome = """
Luann
Alves
       """
print(nome)

sobrenome = "Hamburguer"

print(sobrenome[3 : 10])

#print("Meu nome é %s" % "Luann") *n usar

print("o {} bateu e {}".format("carro", "Explodiu"))

print("o {item1} atravessou a rua e {item2}".format(item1 = "cachorro", item2 = "morreu"))

v = "{:3.2f}".format(699.975000)

print(v)

x = 10
y = 10.1
z = False
w = "Text"

t = (1, 2, 3)
t2 = ([1, 2, 3])

print(type(t2))

t2[0] = 10

print(t2[0])

def retornar_tuple():
    return "Planta", 9, 10.1

p, l, m = retornar_tuple()

print(p, l, m)

list = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(list[3])
print(list[-1])
print(list[0:3])
print(list.index(4))

print(list)
print(list2)

#list.pop(3) #retorna esse valor
list2.append(list.pop(3))

list.append(11)

print(list)
print(list2)

list.remove(11)

print(list)
print(list2)

list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

print(list3[0 : 4])
print(len(list3))
print(min(list3))
print(max(list3))
print(sum(list3))

#sets

print(type(set()))

x1 = set()
x1.add(1)
x1.add(2)

set1 = set("juju")

# | Uniao & Interseccao - Diferença

x3 = {1, 2, 3, 4, 5}
x4 = {6, 7, 8, 9, 10, 56, 12}

print(x3 - x4)

#conjuntos de valores n ordenados
#sets = sequencias mutaveis (nu index)
#frozenset = imutaveis

#Dicionario

"""
Valores imutaveis para chaves em ditc:
int
float
string
tuple
frozenset({1, 2, 3})
até objeto criados(dependendo)
"""

dx = {1: 10, 2: 20, 3: 30}
print(dx[1])
print(dx.get(3))

print(dx.popitem()) #maior valor do meu dic

print(dx.pop(2))

dx[2] = 2222
dx.update({2: "bglh doido"})
dx.update({1: 123123, 2: "churros veio", 3: (1,98)})

#add valor

dx[5] = "dogin"
dx.update({6: 4321, 7: 3.45, 8: "cigarinhuuum"})

print(dx)

#zip ele junta dic tupla list (criando dicts)

print(dict(zip([1,2,3,4,5],["a","b","c","d","e"])))

#enumerate

dict3 = dict(enumerate("Nasa Studio"))
print(dict3)

#um valor

print(dict3.values())
print(dict3.keys())
print(dict3.items())

#if


if tu_e_estudante_sabe_vua== True:
    valor_final = valor_final * 0.5
elif veio == True:
    valor_final = valor_final * 0.3
elif gravida == True:
    valor_final = valor_final * 0.75
else:
    valor_final = valor_final * desc_multiplicador

print("O valor do seu ingresso é de: {}".format(str("{:0.2f}".format(valor_final))))


"""
#Valores booleanos
True False

#Comparativos
1 > 2 = False
1 < 2 = True
1 >= 1 = True
2 <= 3 = True
1 == 2 = False
2 != 12 = True

"Luan" == "Luann" = False

#Operadores logicos
& = E
| = OU
not = NAO

#Operadores de conjuntos
in = contem
not in = nao contem
"""


if "luann" == "Luann":
    print("é igual")
else:
    print("não e igual")
    

devendo = dict(zip(["Luann", "Maria", "Joao"], [1, 2, 3]))

print(devendo)

print(1 in devendo.values())

chave = True
macaneta= True

if not(chave == True) & (macaneta == True):
    print("saiu")
else:
    print("nao saiu")


nomes = ["Luann", "Maria", "Joao"]
aniversarios = ["21/06/2000", "07/02/1991", "15/08/1981"]

nm_niver = tuple(zip(nomes, aniversarios))

for nm, niver in nm_niver:
    print(f"{nm} faz aniversario em {niver}")


x = float(input("Digite um valor "))
y = float(input("Digite outro valor "))

soma = x + y

print("A o resultado da soma é {}".format(soma))