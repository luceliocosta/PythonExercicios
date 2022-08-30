#DESAFIO 045
#Crie um programa que faça o computado jogar Jokenpô com você.
import random as rd
import time as t
print('\033[34m*'*40)
print('\033[34m               JOKENPÔ')
print('\033[34m*'*40)
Jogadas = ['Pedra', 'Papel', 'Tesoura']
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

Você = int(input('Qual é a sua jogada: ').capitalize())
if Você == 0:
    Você = Jogadas[0]
elif Você == 1:
    Você = Jogadas[1]
elif Você == 2:
    Você = Jogadas[2]

Computador = rd.choice(Jogadas)
print('\033[31mJO')
t.sleep(0.5)
print('\033[32mKEN')
t.sleep(0.5)
print('\033[33mPÔ!!!')
t.sleep(0.5)
print('\033[34mO Computador escolheu {} e Você escolheu {}'.format(Computador, Você))
if Você == 'Pedra' and Computador == 'Tesoura':
    print('\033[32mVocê VENCEU. A Pedra ganha da Tesoura ')
elif Você == 'Tesoura' and Computador == 'Pedra':
    print('\033[31mVocê PERDEU. A Pedra ganha da Tesoura')
elif Você == 'Tesoura' and Computador == 'Papel':
    print('\033[32mVocê VENCEU. A Tesoura ganha do Papel')
elif Você == 'Papel' and Computador == 'Tesoura':
    print('\033[31mVocê PERDEU. A Tesoura ganha do Papel')
elif Você == 'Papel' and Computador == 'Pedra':
    print('\033[32mVocê VENCEU. O Papel ganha da Pedra')
elif Você == 'Pedra' and Computador == 'Papel':
    print('\033[31mVocê PERDEU. O Papel ganha da Pedra')
elif Você == Computador:
    print('\033[33mEMPATE!')
else:
    print('\033[33mJOGADA INVÁLIDA!')
