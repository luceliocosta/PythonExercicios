#DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
#mostre o comprimento da hipotenusa.
import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.sqrt(pow(co, 2) + pow(ca, 2))
print('O comprimento da Hipotenusa corresponde a {:.2f}'.format(hip))
