import copy

lista = []
n = int(input(""))

for i in range(0, n):
    a = int(input(""))
    lista.append(a)
    
print(lista[::-1])

lista2 = copy.deepcopy(lista)
x = lista2[-1]
lista2[-1] = lista2[0]
del(lista2[0])
lista2.insert(-1, x)

print(lista2)
print(sorted(lista, reverse = True))

