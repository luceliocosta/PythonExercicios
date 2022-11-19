# DESAFIO 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista

valores = list()
for i in range(0, 5):
    valores.append(int(input(f' Digite um valor para a Posição {i}: ')))
print('-='*30)
print(f'Você digitou os valores: {valores}')
maior = max(valores)
#maior_index = valores.index(maior)
conta_maior = valores.count(maior)
print(f'O maior valor digitado foi  {maior} nas posições ', end='')
if conta_maior >= 1:
    for v in range(0, len(valores)):
        if valores[v] == maior:
            print(v, end='...')

menor = min(valores)
#menor_index = valores.index(menor)
conta_menor = valores.count(menor)
print(f'\nO menor valor digitado foi  {menor} nas posições ', end='')
if conta_menor >= 1:
    for v in range(0, len(valores)):
        if valores[v] == menor:
            print(v,end='...')




