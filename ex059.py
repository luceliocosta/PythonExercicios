#DESAFIO 059
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número número: '))
sair = False
while not sair:
    print('[1] Somar\n'
          '[2] Multiplicar \n'
          '[3] Maior \n'
          '[4] Novos números \n'
          '[5] Sair do programa')
    opção = int(input('Opção: '))
    if opção == 1:
        print(f'Soma: {n1 + n2}')
        sleep(3)
    elif opção == 2:
        print(f'Multiplicação : {n1*n2}')
        sleep(3)
    elif opção == 3:
        maior =max(n1, n2)
        print(f'Maior {maior}')
        sleep(3)
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        sair =True
    else:
        print('Número inválido. Digite novamente!')

    print('=-='*10)
print('Terminando...')
sleep(2)
print('Programa Terminado. Volte sempre!')
