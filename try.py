"""
print('-'*30)
print('{:^30}' .format(' BANCO ATENA '))
print('-'*30)
d = int(input('Qual valor você quer sacar? R$'))
cont_cinquenta = cont_vinte = cont_dez = cont_um = 0
while True:
    while d - 50 >= 0:
        d -= 50
        cont_cinquenta += 1
    while d - 20 >= 0:
        d -= 20
        cont_vinte += 1
    while d - 10 >= 0:
        d -= 10
        cont_dez += 1
    while d - 1 >= 0:
        d -= 1
        cont_um += 1
    break
if cont_cinquenta != 0:
    print(f'Total de {cont_cinquenta} cedulas de R$50')
if cont_vinte != 0:
    print(f'Total de {cont_vinte} cedulas de R$20')
if cont_dez != 0:
    print(f'Total de {cont_dez} cedulas de R$10')
if cont_um != 0:
    print(f'Total de {cont_um} cedulas de R$1')
"""

"""
from math import floor
nota50 = nota20 = nota10 = nota1 = 0
print('{:~^30}'.format( ' Caixa Eletrônico '))
saque = int(input('Digite o valor a ser sacado: '))
while True:
    while saque != 0:
        if saque >= 50:
            nota50 = saque / 50
            nota50 = floor(nota50)
            resto = saque % 50
            saque = resto
        elif saque >= 20:
            nota20 = saque / 20
            nota20 = floor(nota20)
            resto = saque % 20
            saque = resto
        elif saque >= 10:
            nota10 = saque / 10
            nota10 = floor(nota10)
            resto = saque % 10
            saque = resto
        elif saque >= 1:
            nota1 = saque / 1
            nota1 = floor(nota1)
            resto = saque % 1
            saque = resto
    break
print('=-' * 16)
print(f'Será sacado {nota50} cédulas de R$ 50,00.')
print(f'Será sacado {nota20} cédulas de R$ 20,00.')
print(f'Será sacado {nota10} cédulas de R$ 10,00.')
print(f'Será sacado {nota1} cédulas de R$ 1,00.')
"""

"""
saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')
"""

print('='*50)
print(f'{"BANKAST":^50}')
print('='*50)
count50 = n50 = n20 = n10 = n1 = 0
choice = ' '

while True:
    valor = int(input('Quanto você quer sacar? '))
    while True:
        if valor >= 50:
            n50 += 1
            valor-=50

        elif 20 <= valor < 50:
            n20 += 1
            valor -= 20

        elif 10 <= valor < 20:
            n10 += 1
            valor -= 10

        elif 1 <= valor < 10:
            n1 += 1
            valor -= 1

        else:
            break

    if n50 > 0:
        print(f'Total de {n50} notas de R$50.')
    if n20 > 0:
        print(f'Total de {n20} notas de R$20. ')
    if n10 > 0:
        print(f'Total de {n10} notas de R$10.')
    if n1 > 0:
        print(f'Total de {n1} notas de R$1.')

    choice = str(input('Deseja realizar outra operação?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m\nDeseja realizar outra operação?[S/N] ')).upper()[0]

    if choice in 'S':
        n50 = n20 = n10 = n1 = 0
    else: break

print('='*50)
print('Volte sempre ao BANKAST.')
