# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? EU$ '))
novopreco = preco - 0.05 * preco
print('O novo preço com desconto de 5% é igua a EU$ {:.2f}'.format(novopreco))

