def somar(nmr1, nmr2, x = 10, name = "LA"):
    "Funcao somar!"
    return nmr1 + nmr2

atributos = ["__name__", "__module__", "__kwdefaults__", "__defaults__", "__doc__"]

for atributo in atributos:
    print(atributo, " -> ", getattr(somar, atributo))