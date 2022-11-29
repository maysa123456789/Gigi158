'''
#ex8
tam = int(input("Informe o tamanho da lista:"))
lista = []
for i in range(tam):
    valor = int(input("Informe um valor:"))
    lista.append(valor)
print(lista)


#ex9
menor_nu = 5
maior_nu = 0
tam = int(input("Informe o tamanho da lista:"))
lista = []
for i in range(tam):
    valor = int(input("Informe um valor"))
    if valor > maior_nu:
           maior_nu = valor
    if valor < menor_nu:
        menor_nu = valor
    lista.append(valor)
       
print(lista)
media = tam / valor
print("A média é", media)
print("O maior valor é", maior_nu)
print("O menor é", menor_nu)

#ex10
lista = []
for i in range(10):
    number = int(input("Informe um número:"))
    lista.append(number)
print(lista)
'''
#lista2
#ex3
lista = []
for i in range(0, 41, 2):
    lista.append(i)
    
print(lista)

import random
for i in range(6):
    sorteado = random.randint(1,81)
    lista = [sorteado]

print(lista)


