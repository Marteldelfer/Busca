from random import randint as rand
from time import time

#Mais ou menos autoral. Não funciona caso o num não esteja presente na lista

lista = list(range(1_000_000))

def biSearch(lista: list, num: int):
    maximo = len(lista)
    counter = maximo//2
    minimo = 0
    start = time()

    while lista[counter] != num:
        if lista[counter] < num:
            minimo = counter
        elif lista[counter] > num:
            maximo = counter
        counter = (minimo + maximo)//2
    
    print(time() - start)
    return f'{num} na posição {counter}'
    

print(biSearch(lista, rand(1,1000000)))
    
