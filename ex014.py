#DESAFIO 014
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Digite a temperatura em graus Celsius: '))
tf = 1.8*tc + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(tc, tf))


