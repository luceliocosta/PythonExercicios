#DESAFIO 67
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
from time import sleep
while True:
    n = int(input('Queres ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*12)
    for x in range(1, 11):
        print(f'{n} X {x} = {x*n}')
    print('-' * 12)
print('Encerrando o programa ...'), sleep(2)
print('Programa encerrado. Volte sempre! ')
