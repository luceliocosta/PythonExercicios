# DESAFIO 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é igua a {}'.format(n, d))
print('O triplo de {} é igual a {}'.format(n, t))
print('A raiz quadrada de {} é igual a {:.3}'. format(n, r))


