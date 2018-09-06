f1 = 0
f2 = 0

def add():
  global f1, f2
  
  idade = int(input(""))
  if idade <= 2:
    f1 += 1
  else:
    f2 += 1


add()

i = input("")
while i != 'NÂO' and i != 'não' and i != 'Não':
  add()
  i = input("")

total = ((f1 * 9) + (f2 * 6)) * 30

print(total // 100)
print(total % 100)
