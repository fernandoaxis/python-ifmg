soma = 0
print('Informe o preço dos produtos')
for cont in range(10):
	mensagem = 'Produto' + str(cont+1)
	preco = float(input(mensagem))
	soma += preco
media = soma/10
print('O preco medio é ', media)