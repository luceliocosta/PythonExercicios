#DESAFIO 024
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Em que cidade você nasceu?')
x = cidade[:5].strip().lower() == 'santo'
print(x)