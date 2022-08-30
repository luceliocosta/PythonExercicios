#DESAFIO 028
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
x = random.randint(0, 5)
n = int(input('Qual foi o número escolhido pelo computador entre 0 e 5? '))
print('PROCESSANDO...')
sleep(3)
if x == n:
    print('PARABÉNS, Você Venceu!')
else:
    print('Você Perdeu! O número escolhido pelo computador foi {}'.format(x))
