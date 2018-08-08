cont = 0
cont2 = 0
i = 1
a = int(input(""))
b = int(input(""))

while i < 50:
    if a % i == 0:
        cont = cont + 1
    if b % i == 0:
        cont2 = cont2 + 1
    i = i + 1
print(cont + cont2)
