#DESAFIO 066
#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).
somador = contador = 0

while True:

    n = int(input('Digite um valor (Digite 999 para parar): '))
    if n == 999:
        break
    somador = somador + n
    contador = contador + 1
print('Foram digitados {} números  e a soma entre eles vale {}'. format(contador, somador))
