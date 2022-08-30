#DESAFIO 026
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.
frase =str(input('Digite uma frase:')).strip()
conta_a = frase.upper().count('A')
primeiro_a = frase.upper().find('A')
ultimo_a = frase.upper().rfind('A')
print('A letra A aparece {} vezes na frase.'.format(conta_a))
print('A primeira letra A apareceu na posição {}'.format(primeiro_a + 1))
print('A última letra A apareceu na posição {}'.format(ultimo_a + 1))