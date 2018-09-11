def mdc(dividendo, divisor):
  if divisor == 0:
    return dividendo
  else:
    return mdc(divisor, dividendo % divisor)

o = int(input(""))
i = 0
n, m = [], []
while i < o:
  n1, m1 = input("").split()
  n1, m1 = int(n1), int(m1)
  n.append(n1)
  m.append(m1)
  i += 1

for i in range(o):
  print("MDC (",n[i],",",m[i],") =",mdc(n[i], m[i]))
