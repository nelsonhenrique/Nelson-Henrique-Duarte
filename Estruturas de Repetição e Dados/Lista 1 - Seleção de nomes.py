nomes = []
for i in range(10):
  n = input("")
  nomes.append(n)

letra = input("")

for i in nomes:
  if letra in i or letra.swapcase() in i:
    print(i)
