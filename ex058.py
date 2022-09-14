#DESAFIO 058
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
#from time import sleep

x = random.randint(0, 10)
n = int(input('Tenta adivinhar o número escolhido pelo computador entre 0 e 10:  '))
contador = 0
while n != x:
    #print('O número escolhido pelo computador foi {}'.format(x))
    if x > n:
        n = int(input('Mais...Tente outra vez: '))
    else:
        n = int(input('Menos...Tente outra vez: '))
    contador = contador + 1
print('PARABÉNS, Você Venceu com {} tentativas! O número escolhido pelo computador foi {}'.format(contador, x))
