#DESAFIO O26
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input(' Qual é o seu nome completo? ')).strip().lower()
print('Seu nome tem Silva? ', end='')
print('silva' in nome)
