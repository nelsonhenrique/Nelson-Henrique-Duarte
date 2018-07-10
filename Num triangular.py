i = 1
j = 0
n = int(input("Digite o número: "))

while j < n:
    j = i * (i + 1) * (i + 2)
    i = i + 1

if j == n:
    print(i-1," * ",i, " * ",i+1)
    print("Verdadeiro")
else:
    print("Falso")
