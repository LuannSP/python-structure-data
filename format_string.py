nome = "Luann Alves"

print(
    f'Qual é o mais brabo {nome.upper() + "!" * 3 }')

x = 1.0
y = 2.1

print(f'a soma de {x} com {y} é de: {x+y}')

dict = ({"Nome": "Luann", "Ocupacao": "Software Enginner"})

print(f'O {dict["Nome"]} trabalha com {dict["Ocupacao"]}')

nome = "Luann"
ocupacao = "Programmer Junior"
idade = 21

print(
    f'Nome: {nome}\n'
    f'Ocupação: {ocupacao}\n'
    f'Idade: {idade}'
)


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca}/{self.modelo} - Ano {self.ano}"

    def __repr__(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Ano: {self.ano}"
        )


possante = Carro('Ferrari', 'F8 Tributo', '21')

print(f'{possante}')  # exibindo como acima

print(f'{possante!r}')  # exibindo por cada atributo

###

valor = 5.5 / 40.1

print(
    f'Resultado original {valor}\n'
    f'Resultado formatado {valor:.2%}'
)

''' 
Explicando:

O .1 diz que a string resultante deve ter apenas uma casa decimal;
O % multiplica o valor por 100 e inclui o % ao final.
'''
