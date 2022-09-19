#DESAFIO 68
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint as rani
somador_vitoria = 0
print('=-'*20)
text = 'JOGO PAR OU ÍMPAR'
print(f'           {text}')
print('=-'*20)
while True:
    computador = rani(1, 10)

    n = int(input('Digite um valor : '))
    soma = computador + n
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('=-' * 20)
    print(f'Você jogou {n} e o computador {computador}. Total de {soma} deu par' if soma % 2 == 0
          else f'Você jogou {n} e o computador {computador}. Total de {soma} deu ímpar')
    print('=-' * 20)
    if soma % 2 == 0 and opção == 'P' or soma % 2 != 0 and opção == 'I':
       print('Você Venceu!')
       print('Vamos jogar novamente...')
       somador_vitoria += 1
    else:
       print('Você Perdeu!')
       break
print(f'GAME OVER! Você Venceu {somador_vitoria} vezes' if somador_vitoria == 1 else 'GAME OVER! Você Venceu {} vezes' .format(somador_vitoria) )






