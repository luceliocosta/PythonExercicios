#DESAFIO 027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digita o seu nome completo: ')).strip()
dividido = nome.split()
tamanho = int(len(dividido))
print(dividido)
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[tamanho - 1]))