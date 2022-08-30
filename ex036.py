#DESAFIO 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# será negado.
print('\033[31m*'*40)
print('\033[31m         Empréstimo Bancário')
print('\033[31m*'*40)
casa = float(input('Por favor, Poderia informar-nos o valor da casa que deseja comprar: $'))
salario = float(input('Por favor, Poderia informar-nos o seu salário: $'))
anos = int(input('Em quantos anos deseja pagar: '))
prestmensal = casa/(12*anos)
#print(prestmensal)
print('Para pagar uma casa de ${:.2f} em {} anos a prestação será de ${:.2f}'.format(casa, anos, prestmensal))
if prestmensal > 0.30*salario:
    print('O seu empréstimo foi RECUSADO!')
else:
    print('O seu empréstimo foi ACEITE')



