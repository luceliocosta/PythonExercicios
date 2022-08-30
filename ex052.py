#DESAFIO 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))

if n == 2:
    print(f'O número {n} é um número PRIMO!')
elif n == 1:
    print(f'O número {n} não é um número PRIMO!')
else:
    for x in range(2, n):
        if n % x == 0:

            print(f'O número {n} não é um número PRIMO!')
            break

    if x == n-1: # Se terminar a sequência faça
        print(f'O número {n} é um número PRIMO!')

