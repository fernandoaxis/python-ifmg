def cubo(num):
	return num * num * num
	print('num ao cubo é ', cubo)

n = float(input('Informe um numero'))
print(n, ' ao cubo e ', cubo(n))
print(n, ' elevado a nona é ', cubo(cubo(n)))
