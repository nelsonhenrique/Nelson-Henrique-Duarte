def par(lista):
    l = []
    
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero % 2 == 0:
            l.append(numero)
        l = l + par(lista)
    
    return l

o = int(input(""))
n = list(range(o))
pares = list(par(n))

for i in pares:
  print(i)
