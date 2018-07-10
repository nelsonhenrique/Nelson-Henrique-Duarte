def printf (text):
    print(text, end="")

num = int(input(""))
invertido = 0
z = str(num)
x = ''
sla = ''

while num > 0:
    invertido = invertido * 10 + num % 10
    num = num // 10
    if invertido > 0:
        x = str(invertido)

if len(z) == len(x):
    print(invertido)
else:
    sla = x.zfill(len(z))
    for i in sla:
        printf('['+i+']')

