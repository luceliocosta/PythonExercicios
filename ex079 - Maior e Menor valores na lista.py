# DESAFIO 079 - Resolução alternativa
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respetivas posições na lista.
valores = list()
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {v}: ')))
print(f'A sua lista contém os seguintes valores: {valores}')
for v in range(0, len(valores)):
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores [v] > maior:
            maior = valores[v]
        if valores [v] < menor:
            menor = valores[v]
print(f'Maior valor na lista: {maior}')
print(f'Menor valor nalista: {menor}')





