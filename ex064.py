#DESAFIO 064
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

#n = int(input('Digite um número: '))
somador = n = 0
contador = -1
while n != 999:
    somador = somador + n
    contador = contador + 1
    n = int(input('Digite um número [Digite 999 para parar]: '))

print('Foram digitados {} números  e a soma entre eles vale {}'. format(contador, somador))

