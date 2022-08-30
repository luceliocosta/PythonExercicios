#DESAFIO 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Informe o número: '))
unidade = n % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000
print('Unidade:{}'.format(unidade))
print('Dezena:{}'.format(dezena))
print('Centena:{}'.format(centena))
print('Milhar:{}'.format(milhar))



