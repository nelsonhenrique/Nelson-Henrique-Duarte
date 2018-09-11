def f1(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]

def f2(n):
    if n == 0:
        return ''
    else:
        return f2(n//2) + str(n%2)

n = int(input(""))
print(f2(n))
