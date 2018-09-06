vida = 100
regen = 0
tempo = []

x = int(input(""))

for i in range(x):
  
  d, t = input("").split()
  d = int(d)
  t = int(t)
  vida = vida - d
  tempo.append(t)

regen = max(tempo) - min(tempo) 

y = int(input(""))

regen = regen * y
vida = vida + regen

if vida > 0:
  print("Inimigo Vivo")
else:
  print("Inimigo Morto")
