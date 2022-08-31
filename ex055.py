#DESAFIO 055
#  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#maior = 0

for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}º pessoa: '))
    if x == 1:
        menor = peso
        maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido equivale a {}Kg'.format(maior))
print('O menor peso lido equivale a {}Kg'.format(menor))


