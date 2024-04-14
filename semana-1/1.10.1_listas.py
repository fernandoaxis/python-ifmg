"""
.append(x) Adiciona o elemento x no final da lista l
l.insert(p, x) Insere o elemento x na posição p da lista l
l.pop(p) Remove e retorna o elemento da posição p de l (se p não for
informado, a última posição é considerada)
l.clear() Remove todos os elementos da lista l

"""

soma = 0
lista_produtos = []
print('Informe o preco dos produtos')
for cont in range(10):
	mensagem = 'Produto ' + str(cont+1) + ': '
	nome = input('Nome: ')
	preco = float(input(mensagem))
	soma += preco
	lista_produtos.append(preco)

media = soma/10

print('O preco medio é ', media)
print('Os precos acima da media sao: ')

for produto in lista_produtos:
	nome, preco = produto
	if preco > media:
		print('Produto: ', nome)
		print('Preço: ', preco)
