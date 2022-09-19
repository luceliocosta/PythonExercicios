#DESAFIO 069
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o utilizador quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
conta_mais_de_18 = 0
conta_homens = 0
conta_mulher_menos_de_20 = 0
while True:
    print('-'*20)
    print('Cadastro de Pessoas')
    print('-'*20)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digiteo seu sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        conta_mais_de_18 = conta_mais_de_18 + 1
    if sexo == 'M':
        conta_homens = conta_homens + 1
    if sexo == 'F' and idade < 20:
        conta_mulher_menos_de_20 = conta_mulher_menos_de_20 + 1

    option = ' '
    while option not in 'SN':
        option = str(input('Quer continuar: [S/N]')).strip().upper()[0]

    if option == 'N':
        break
print('-'*30)
print('ANÁLISE DOS DADOS CADASTRADOS')
print('-'*30)

print(f'Há {conta_mais_de_18} pessoas com mais de 18 anos de idade')
print(f'Ao total {conta_homens} homens foram cadastrados')
print(f'Existem {conta_mulher_menos_de_20} mulheres com menos de 20 anos')
print('-'*30)
