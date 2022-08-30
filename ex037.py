#DESAFIO 37
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('[1]-Converter em binário')
print('[2]-Converter em Octal')
print('[3]-Converter em Hexadecimal')
base = int(input('Digite a base de conversão: '))

if base == 3:
    hexconv = hex(num)[2:]
    print(f'A conversão de {num} em hexadecima é igual a {hexconv}')
elif base == 1:
    binconv = bin(num)[2:]
    print(f'A conversão de {num} em binário é igual a {binconv}')
elif base == 2:
    octconv = oct(num)[2:]
    print(f'A conversão de {num} em Octal é igual a {octconv}')
else:
    print('O número Digitado não é válido!')
