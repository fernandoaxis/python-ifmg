# _*_ coding: utf-8 _*_

HIST = ''

def calcula(expr):
	try:
		return eval(expr)
	except:
		print('Expressao invalida')
		return None

def historico(expr, res):
	global HIST
	if res is not None:
		HIST += '\n\n' + expr
		HIST += '\n' + str(res)

def principal():
	while True:
		print('Infome a expressao matematica')
		print('(h para historico, s para sair)')

		expr = input()
		if expr.lower() == 's':
			break
		if expr.lower() == 'h':
			print(HIST, '\n')
		else:
			res = calcula(expr)
			historico(expr, res)
			print(res, '\n')

if __name__ == '__main__':
	principal()