soma = 0
while True:
	n = float(input('Informe um numero: '))
	if n < 0:
		continue
	if n == 0:
		break
	soma = soma + n
print('soma dos numeros: ', soma)