#DESAFIO 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um número para calcular o seu fatorial: '))
m = n
print(f'Calculando {n}! = ', end='')
while n != 1:
    print(n, end=' x ')
    n = n - 1
    m = m*n
print('1 =', m)
