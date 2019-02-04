a = input("")
a = a.split()
lista = []
par = []

lista = [int(i) for i in a]

for i in lista:
    if i % 2 == 0 and i >= 0:
        par.append(i)
if len(par) == 0:
    print("-1")
    
resul = sum(par)/len(par)

print('{:.2f}'.format(resul))
