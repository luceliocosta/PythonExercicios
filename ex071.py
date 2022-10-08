# DESAFIO 71
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print('='*40)
info = 'MULTIBANCO COSTA [MBC]'
print('{:^40}'.format(info))
print('='*40)
valor = int(input('Que Valor você quer levantar? R$'))
resto_50 = resto_20 = resto_10 = resto_1 = valorfinal = valor

while True:

    if valor >= 50:
        conta_50 = int(valor / 50)
        resto_50 = valorfinal = valor % 50
        if conta_50 != 0:
            print('Total de {} notas de R$50'.format(conta_50))
        #print(resto_50)

    if valor >= 20:
        conta_20 = int(resto_50 / 20)
        resto_20 = valorfinal = resto_50 % 20
        if conta_20 != 0:
            print('Total de {} notas de R$20'.format(conta_20))
        # print(resto_20)

    if valor >= 10:
        conta_10 = int(resto_20 / 10)
        resto_10 = valorfinal = resto_20 % 10
        if conta_10 != 0:
            print('Total de {} notas de R$10'.format(conta_10))

    if valor >= 1:
        conta_1 = int(resto_10 / 1)
        resto_1 = valorfinal = resto_10 % 1
        if conta_1 != 0:
            print('Total de {} notas de R$1'.format(conta_1))

    if valorfinal == 0:
        print('=' * 40)
        print('Volte Sempre ao Banco Costa! Tenha um excelente dia!')
        break




