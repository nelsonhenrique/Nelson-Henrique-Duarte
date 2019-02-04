lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
comp = []

for i in lista1:
    if i in lista2:
        comp.append(i)
        
if len(comp) > 0:
    for i in comp:
        print(i)

else:
    print("VAZIO")
