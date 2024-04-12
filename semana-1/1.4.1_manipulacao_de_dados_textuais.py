"""
1.4

-> funcoes 

abs(n) - retorna o valor absoluto de n
chr(n) - retorna o caractere representado pelo numero n
ord(c) - retorna o codigo correspondente ao caractere c
round(n,d) - arredonda n considerando d casas decimais
type(o) - retorna o tipo de o 

"""


#1.4.1

"""
	funcoes:

	s.find 
	s.format
	s.lower
	s.replace
"""
nome_completo = input('Informe seu nome completo: ')
sobrenome = input('Informe seu sobrenome: ')

pos = nome_completo.find(sobrenome)

if pos != -1:
	print('Seu sobrenome começa na posição ', pos)
else:
	print('Sobrenome não encontrado')

n = float(input('Informe um numero: '))
print('{n:.8f}'.format(n=n))