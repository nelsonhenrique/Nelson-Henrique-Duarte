inicial = int(input(""))
final = int(input(""))

for i in range(inicial, final):
    if i % 100 != 0 and i % 4 == 0 or i % 400 == 0:
        print(i)
