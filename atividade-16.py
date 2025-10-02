# Converta a tupla (5, 8, 12) em uma lista, adicione o número 20 e converta de volta em tupla.

tupla = (5, 8, 12)
lista = list(tupla)
lista.append(20)
tupla = tuple(lista)
print(tupla)