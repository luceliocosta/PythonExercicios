#DESAFIO 065
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
n = int(input('Digite um número: '))
option = str(input('Gostaria de continuar: [s/n]')).strip().lower()
while option not in 'sn':
    option = str(input('Digite um valor válido. Gostaria de continuar: [s/n]')).strip()

maior = menor = somador = n
cont = 1
#option = 'n'
while 'n' not in option:
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    somador = somador + n
    option = str(input('Gostaria de continuar: [s/n]')).strip().lower()
    while option not in 'sn':
        option = str(input('Digite um valor válido. Gostaria de continuar: [s/n]')).strip()
media = somador/cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, float(media)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


