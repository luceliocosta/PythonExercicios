#DESAFIO 015
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dist = float(input('Qual é a quantidade de Km que você percorreu? '))
ndias = int(input('Qual é o número de dias que o carro foi alugado? '))
custo_dia = 60 * ndias
custo_dist = 0.15 * dist
precoapagar = custo_dia + custo_dist
print('O preço total a pagar correspondente a {}Km de distância percorrida e {} dia de waluguel corresponde a R${}.'.format(dist, ndias, precoapagar))