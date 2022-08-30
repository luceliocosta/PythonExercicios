# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere: US$ 1,00 = R$ 3,27

money = float(input('Quanto dinheiro tens na carteira R$? '))
print('Com R$ {} podes comprar US$ {:.2f}'.format(money, money/3.27))



