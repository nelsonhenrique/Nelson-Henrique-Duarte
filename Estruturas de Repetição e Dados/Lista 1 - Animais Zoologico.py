qtdC = 0
qtdM = 0
mediaT = 0
pesoT = 0
qtdT = 0
def add():

  tipo = input("")
  peso = float(input(""))
  pais = input("")

  if tipo == 'macaco':
    global qtdM
    qtdM = qtdM + 1
  elif tipo == 'cobra' and pais == 'Venezuela':
    global qtdC
    qtdC = qtdC + 1
  elif tipo == 'tigre':
    global pesoT
    global qtdT
    pesoT = pesoT + peso
    qtdT = qtdT + 1
  
add()

i = input("")

while i == 'continuar':
  add()
  i = input("")

print(qtdM)
if qtdT != 0:
  mediaT = pesoT / qtdT
else:
  mediaT = 0
print(round(mediaT, 2))
print(qtdC)
