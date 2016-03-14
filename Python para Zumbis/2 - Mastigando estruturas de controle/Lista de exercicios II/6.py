'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Obseerve que Salário bruto - descontos = Salário Líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    a. +Salário Bruto: R$
    b. -IR(11%): R$
    c. -INSS(8%): R$
    d. -Sindicato(5%): R$
    e. =Salário Liquido: R$
'''
ganho_hora = float(input('Digite o quanto você ganha por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))
salario = ganho_hora * horas
ir = salario * 11/100
inss = salario * 8/100
sindicato = salario * 5/100
descontos = ir + inss + sindicato
liquido = salario - descontos

print ('+Salário Bruto:\t\t R$ %10.2f' %salario)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sindicato)
print ('+Salário Líquido:\t R$ %10.2f' %liquido)
print ('Total de Descontos:\t R$ %10.2f' %descontos)



