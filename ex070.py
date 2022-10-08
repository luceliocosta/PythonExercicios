#DESAFIO 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o utilizador vai continuar
# ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-'*20)
print('    Costa Company')
print('-'*20)

totcompra = acima_1000 = cont = 0
nome = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))

    totcompra = totcompra + preço

    if preço > 1000:
        acima_1000 = acima_1000 + 1

    if cont == 0:
        menor = preço
        nome = produto
        cont = cont + 1

    if preço <= menor:
        menor = preço
        nome = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('{:-^60}'.format(' ANÁLISE DE DADOS '))
print(f'O total gasto na compra vale: {totcompra:.2f} R$')
print(f'Ao todo {acima_1000} produtos custam acima de R$1000.00')
print(f'O produto mais barato chama-se {nome} e custa R${menor:.2f}')
print('{:-^60}'.format(' FIM DO PROGRAMA '))
