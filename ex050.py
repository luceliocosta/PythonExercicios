#DESAFIO 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for x in range(1, 7):
    num = int(input(f'Digite o {x}º número: '))
    if num % 2 == 0:
        soma = soma + num
        contador += 1
print(f'Você informou {contador} números pares e a soma foi {soma} ')

