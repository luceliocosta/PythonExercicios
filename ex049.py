#DESAFIO 049
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número: '))
print('{:=^40}'.format('TABUADA'))
for x in range(1, 13):
    print('{} x {:2} = {}'.format(n, x, n * x))
print('='*40)