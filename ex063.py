#DESAFIO 063
#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci.
"""
import math
n = int(input('Digite um número inteiro: '))

cont = 0
while cont != n:
    alpha = ((1 + math.sqrt(5)) / 2)
    beta = ((1 - math.sqrt(5)) / 2)
    fn = (math.pow(alpha, cont) - math.pow(beta, cont)) * 1 / math.sqrt(5)

    print('{} -> '.format(int(fn)), end='')
    cont += 1
print('Fim')
"""
print('-'*24)
print(' Sequência de Fibonacci')
print('-'*24)
n = int(input('Quantos termos gostarias de mostrar: '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= n:
    t3 = t2 + t1
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3

    cont = cont + 1
print('FIM')






