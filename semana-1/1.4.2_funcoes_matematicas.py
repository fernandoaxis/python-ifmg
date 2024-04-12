"""
	celi(x) -> retorna o teto de x
	floor(x) -> retorna o piso de x
	trunc(x) -> retorna parte inteira de x
	exp(x) -> retorna e elevado a x
	log(x,b) -> retorna o logaritimo de x em uma base b, se a base nao for especificada retorna o logaritmo natural de x
	sqrt(x) - > retorna raiz quadrada de x
	pi -> retorna o valor de pi

"""

import math

n = float(input('Infome um numero: '))
x = n * math.pi

print('x = n * pi = ', x)
print('teto de x = ', math.ceil(x))
print('x = n * pi = ', math.floor(x))
print('x = n * pi = ', math.log(x,10))
print('raiz de x = ', math.sqrt(x))

