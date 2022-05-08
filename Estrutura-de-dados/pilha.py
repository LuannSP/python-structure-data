"""
peek = retornar uma lista vazia quando acabar os dados na pilha se tiver dados retorna o dado do topo
iter = iteracoes (for)
next = parar a iteracao para nao dar indexerror (for)
bool = quando acabar os dados retorna false (while)
repr = representacao da classe
"""
from __future__ import annotations
from typing import List, Any
from copy import deepcopy


class Pilha:

    def __init__(self) -> None:
        self.__dados: List[Any] = []
        self.__index = 0

    def push(self, elemento: Any) -> None:
        self.__dados.append(elemento)

    def pop(self) -> Any:
        return self.__dados.pop()

    def peek(self) -> Any:
        if not self.__dados:
            return []
        return self.__dados[-1]

    def __iter__(self) -> Pilha:
        self.__index = len(self.__dados)
        return self

    def __next__(self) -> Any:
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__dados[self.__index]

    def __bool__(self) -> bool:
        return bool(self.__dados)

    def __repr__(self) -> str:
        return f"{self.__dados}"


"""
p = Pilha()

p.push(1)
p.push(2)
p.push(3)

print(p)

p.pop()
p.pop()
p.pop()

print(p)

p.push(1)
p.push(2)
p.push(3)

for dados in p:
    print(dados)

p_copia = deepcopy(p)

while p_copia:
    print(p_copia.pop())
"""
