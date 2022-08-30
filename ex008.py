# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros.

v = float(input('Digite um valor em metros: '))
vcm = v*100 # Conversão de v em cm
vmm = v*1000 # Conversão de v em mm
print('A conversão de {} m em cm é igual a {}'.format(v, vcm))
print('A conversão de {} m em mm é igual a {}'.format(v, vmm))



