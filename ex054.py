#DESAFIO 054
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
import datetime
diminuidor = 7
anoactual = datetime.date.today().year
for x in range(7):
    anodenasc = int(input(f'Digite o ano de nascimento da {x + 1}º pessoa: '))
    if anoactual - anodenasc >= 18:
        diminuidor = diminuidor - 1
print(f'{diminuidor} pessoas ainda não atingiram a maior idade e {7 - diminuidor} pessoas já atingiram a maior idade')
