#DESAFIO 018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
x = float(input('Dite um angulo qualquer: '))
y = math.radians(x)
print('O Seno de {} é igual a {:.2f}'.format(x, math.sin(y)))
print('O Coseno de {} é igual a {:.2f}'.format(x, math.cos(y)))
print(' A Tangente de {} é igual a {:.2f}'.format(x, math.tan(y)))





