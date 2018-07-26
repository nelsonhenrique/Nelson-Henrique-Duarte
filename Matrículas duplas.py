p2 = []
p3 = []
lista = []

i = 0
j = 0

while i < 45:
    a = int(input(""))
    p2.append(a)
    i = i + 1

while j < 30:
    b = int(input(""))
    p3.append(b)
    j = j + 1

for i in p2:
    if i in p3:
        lista.append(i)
print(lista)
