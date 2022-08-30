#DESAFIO 046
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep as sp
import emoji

for x in range (10, -1, -1):
    sp(1)
    print(x)
sp(1)
print(emoji.emojize(':sparkler:'*20))
