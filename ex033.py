#DESAFIO 33
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#import math as m
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#maior = max(n1, n2, n3)
#menor = min(n1, n2, n3)
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número é o ', maior)
print('O menor número é o ', menor)
