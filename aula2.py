"""

def calcular_preco_cinema(preco_bilhete, multiplicador):
    return preco_bilhete * multiplicador

preco_bilhete = 10
multiplicador = 1
idade = 32
isGravida = True

if idade >= 80:
    multiplicador = 0.7
elif isGravida:
    multiplicador = 0.75

print(f"O preço do ingresso é: {str(calcular_preco_cinema(preco_bilhete, multiplicador))}")

def funcaodoida():
    print("")

def somar(nmr1, nmr2):
    return nmr1 + nmr2

def multiplicar(nmr1, nmr2, function):
    return function(nmr1,nmr2)

def multiplicador(nmr1, nmr2):
    return nmr1 * nmr2

print(multiplicar(10 , 10, multiplicador))

x = lambda nmr1, nmr2: nmr1 * nmr2

print(multiplicar(10, 10, x))

# Parâmetros posicionais
# Parâmetros facultativos
    # Um dos últimos parâmetros
# Parâmetros de palavras-chave
# Parâmetros de posição variável
# Parâmetros de palavras-chave de posição variável
# Argumento somente de palavras-chave

from ast import arg
import re


def sm(nmr1, nmr2, msg = ""):
    print(msg)
    return nmr1 / nmr2

print(sm(nmr1 = 2, nmr2 = 1, msg = "O resultado é:"))

print(sm(2, nmr2 = 1, msg = "O resultado é:"))

print(sm(2, 1,"O resultado é:"))

print(sm(1, 2))

#################################################

def sm2(*args):
    resultado = 0
    for num in args:
        resultado += num
    print(f"O resultado é: {resultado}")
         
#sm2(1, 2, 3, 4, 5, 6, 7, 8)

#nmr = (1, 2, 3, 4, 5, 6, 7, 8)

#sm2(*nmr)

def printi(*args):
    for nmr in args:
        print(nmr)
        print(type(nmr))

printi(1, 2.5, "Str", True, (1, 2), {"a": 1}, [1, 2])

#####################################################

#args = empacotar/desempacotar pra uma lista/tupla
#kwargs = empacotar/desempacotar pra um dict

def sm3(**kwargs):
    print(kwargs)
    print(type(kwargs))

sm3(a = 1, b = 2, c = 3)

dict = {"a": 1, "b": 2, "c": 3}

sm3(**dict)

#n é mt usado

def param_somentePalavraChave(*args, c):
    print(args, c)

param_somentePalavraChave(1, 2, c = 5)

"""