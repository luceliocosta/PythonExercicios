# DESAFIO 075
#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (int(input('Digite um valor: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores : {valores}')
print(f'O número nove apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
contPares = 0
print('Os números pares digitados são: ', end=' ')
for val in valores:
    if val % 2 == 0:
        print(val, end=' ')
        contPares = contPares + 1
if contPares == 0:
    print('Não foi digitado nenhum número Par')


