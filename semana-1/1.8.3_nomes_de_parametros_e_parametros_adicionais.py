def juros(capital, taxa, tempo=12):
	return (capital * taxa * tempo)

print('Calculo de juros')

cap = float(input('Capital: '))
tax = float(input('Taxa: '))
tem = input('Tempo(Deixe em branco para o padrao de 12)')

if tem == '':
	jur = juros(cap, tax)
else:
	tem = float(tem)
	jur = juros(taxa=tax, capital=cap,tempo=tem)
print('O valor dos juros é ', jur)

