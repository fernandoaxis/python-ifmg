import os

print('Contatos cadastrados: ')

if not os.path.isfile('contatos.txt'):
	print('Arquivo não encontrado')
else:
	arq = open('contatos.txt')
	linhas = arq.readlines()

	for contato in linhas:
		print(contato.strip())
	arq.close()
	print('-' * 50)

	arq = open('contatos.txt')
	while True:
		contato = arq.readline()
		if contato == '':
			break;

		print(contato.strip())
	arq.close()
	print('-' * 50)

	arq = open('contatos.txt')
	print(arq.read().strip())
	arq.close()