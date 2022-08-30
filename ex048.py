#DESAFIO 048
#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500
soma = 0
contador = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        print(x, end=' ')
        contador = contador + 1
        soma = soma + x
print(f' \n A soma de todos os {contador} números ímpares  que são múltiplos de três é igual a {soma}')
