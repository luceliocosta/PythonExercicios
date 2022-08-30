#DESAFIO 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
an = 0
#print(a1)
for x in range(1, 11):
    if x == 1:
        an = a1
        print(an, end=' -> ')
    else:
        an = an + r
        print(an, end=' -> ')
print('FIM')


