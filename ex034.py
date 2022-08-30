#DESAFIO 34
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o seu salário em? $ '))
if salario > 1250:
    aumento = 1.1*salario
else:
    aumento = 1.15*salario
print('O seu novo salário é igual a ${:.2f}'.format(aumento))







