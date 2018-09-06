qtdcN = 0
qtdcE = 0
diasN = 0
diasE = 0
precoN = 0
precoE = 0
x = int(input(""))

for i in range(x):
  peso = int(input(""))
  tipo = int(input(""))
  dist = int(input(""))

  if tipo == 0:
    while peso > 0:
      peso = peso - 10
      qtdcN += 1
      precoN = qtdcN * 500
    while dist > 0:
      dist = dist - 100
      diasN += 1
  elif tipo == 1:
    while peso > 0:
      peso = peso - 5
      qtdcE += 1
      precoE = qtdcE * 1200
    while dist > 0:
      dist = dist - 250
      diasE += 1    

c = qtdcN + qtdcE
p = precoE + precoN

if diasE > diasN:
  d = diasE
else:
  d = diasN

print(c, p, d)
