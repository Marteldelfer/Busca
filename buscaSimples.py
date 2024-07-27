from random import randint as rand
from time import time

lista = list(range(1_000_000))
lista.sort()

num = rand(1,1_000_000)

def busca(lista: list, num: int):
    start = time()
    count: int = -1
    for i in lista:
        count += 1
        if num == i:
            print(time() - start)
            return f'{num} está na posição {i}'
        elif i > num:
            print(time() - start)
            return None
        
print(busca(lista, num))        