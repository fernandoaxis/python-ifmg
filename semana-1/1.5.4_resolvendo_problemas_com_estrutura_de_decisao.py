"""

1) Ler os termos A, B e C;

2) Garantir que temos uma equação de segundo grau testando se A é diferente de zero;

3) Se for uma equação de segundo grau, calculamos o delta (∆ = B² − 4 × A × C);

4) Após o cálculo, temos três situações para o delta:

• Se o delta for menor que zero, a equação não possui raízes;
• Se o delta for igual a zero, então a equação possui uma única raiz;
• Por fim, se o delta é maior que zero temos duas raízes
 X1=−B+√∆/2×A e X2=−B−√∆/2×A

"""

import math
print('Informe os termos da equação Ax² + Bx +C')

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a == 0:
    print('Não é uma equação de segundo grau')
else:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print('A equação não tem raízes')
    elif delta == 0:
        x1 = b * (-1) / (2 * a)
        print('A equação possui a raiz:', x1)
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (b * (-1) + raiz_delta) / (2 * a)
        x2 = (b * (-1) - raiz_delta) / (2 * a)

        print('A equação possui duas raízes: ')
        print('x1 = ', x1)
        print('x2 = ', x2)











