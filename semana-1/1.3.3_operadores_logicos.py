n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))

p = (n1 > n2)
q = (n1 != n2)

r = not (p or q) and (not p)

print('p =', p)
print('q =', q)
print('r =', r)

