salario = int('Salario? ')
imposto = float('Imposto em % (ex: 27.5)? ')

if imposto == '':
	imposto = 27.5
else: 
	imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))