#DESAFIO 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))
resto = n % 2
if resto == 0:
    print('{} é um número Par'.format(n))
else:
    print('{} é um número Ímpar'.format(n))
