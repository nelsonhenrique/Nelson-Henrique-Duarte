def ant (n):
    if n <= 1:
        return n
    else:
        return ant(n-1) + ant(n-2)

n = int(input(""))
if n == 0:
  print("O antidoto nao e necessario")
else:
  print(ant(n),"mg/L")
