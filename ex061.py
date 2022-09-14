#DESAFIO 061
#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while

a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
an = a1
contador = 1
while contador < 11:
    print('{} -> '.format(an), end='')
    an = an + r
    contador = contador + 1
print('FIM')