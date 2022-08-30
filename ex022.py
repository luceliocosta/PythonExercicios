# DESAFIO 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Escreva o seu nome completo: ')
print('Nome com todas as letras em Maiúsculas:', end=' ')
print(nome.lstrip().upper())
print('Nome com todas as letras em minúsculas:', end=' ')
print(nome.lstrip().lower())
print('Ao todo tem {} letras sem consideram o espaço'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))


