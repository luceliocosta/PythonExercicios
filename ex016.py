#DESAFIO 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
from math import trunc
n = float(input('Digite um número: '))
parteinteira = math.trunc(n)
#i = int(n)
print('A portção inteira de {} corresponde a {}'.format(n, parteinteira))



