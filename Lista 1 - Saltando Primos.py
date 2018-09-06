primos = []
l, u = input("").split()
l = int(l)
u = int(u)

divisores =[]
for i in range(l, u+1): 
    for j in range(1, i+1):
        if i >= j:
            if i % j == 0:
                divisores.append(j)        
    if len(divisores) == 2:
        primos.append(i)
    divisores = []

v = []

for i in range(1, len(primos)):
  v.append(primos[i] - primos[i-1])

m = 0
c = 0


if len(v) == 0:
  print("-1", "\n")

elif len(primos) > 0:
  resul = primos[0]
  for i in v:
    for j in v:
      if i == j:
        c += 1
    if c > m:
      m = c
      resul = i
    c = 0

  print(resul, "\n")
