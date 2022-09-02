#DESAFIO 057
#: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo: [M/F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido. Digite novamente!')
print(f'Sexo {sexo} registdo com sucesso!')
'''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido. Digite Novamente: [M/F] '))



