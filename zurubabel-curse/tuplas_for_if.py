'''

nomes = ["Maria", "João"]
idades = [34, 23]

nomes_idades = tuple(zip(nomes, idades))

for nome, idade in nomes_idades:
    print("{} tem {} anos".format(nome, idade))

retorno = ""
i = 0

for x in "computador":
   retorno += x
   i += 1
   if i > 3:
       print(retorno)
       retorno = ""
       i = 0
else:
    print(retorno)

list = [("Luann", "Alves"), ("Maria", "João")]

for x in list:
    print(x)
    for y in x:
        print(y)
        for z in y:
            print(z)

for x in range(100):
    if x % 2 == 0:
        print("O numero {} é par".format(x))
    else:
        print("O numero {} é impar".format(x))

i = 0

while i < len("Luann"):
    print("Luann"[i])
    i += 1
else:
    print("Fim do while")



clientes = ["Maria", "Joao", "Neto", "Manu", "Junin"]
banidos = "Junin"

shuffle(clientes)

for cliente in clientes:
    if cliente == banidos:
        print("{} não entrou.".format(cliente))
        continue
    print("{} entrou".format(cliente))
    
'''

from random import shuffle, random

clientes = ["Maria", "Joaozinho", "kleber", "Anne", "Jhonata", "Gabi"]
produtos = ["Ovo", "Pizza", "Refri", "Cerveja de milho", "Bacon velho"]

alergia = "Ovo"
blacklist = "Anne"
morreu = False

for cliente in clientes:
    morreu = False
    if cliente == blacklist:
        print(f"{cliente} não pode entrar aqui vacilão\n")
        continue
    print(f"{cliente} entrou no boteco")

    for produto in produtos:
        shuffle(produtos)
        print(f"----{cliente} consumiu {produto}")
        if (produto == alergia) & (random() > 0.7):
            morreu = True
            break
        if random() > 0.5:
            print(f"---- {cliente} bate um papo furado com meias verdades")
        else:
            print(f"---- {cliente} pobre e grosso(a)")

    if morreu:
        # print(f"{cliente} murreu.!\n")
        # continue
        print(f"O {cliente} murreu e os homi chegaram e fecharam meu buteco, eu sou trabalhador muço")
        break

    print(f"{cliente} saiu do boteco sem pagar\n")