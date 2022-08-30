#DESAFIO 032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite o Ano: '))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
        print('O Ano {} não é BISSEXTO!'.format(ano))
elif ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O Ano {} não é BISSEXTO!'.format(ano))

