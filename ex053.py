#DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#frase = str(input('Escreva qualquer coisa: ')).lower().replace(' ', '').strip()
"""
f = []

for c in range(len(frase) - 1, -1, -1):
    a = frase[c]
    f.append(a)
invert = ''.join(f)
print(f'O inverso de {frase} é {invert} ')
if frase == invert:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

    """

# Forma mais fácil

frase = str(input('Escreva qualquer coisa: ')).lower().replace(' ', '')
invert_frase =frase[::-1]
print(f'O inverso de {frase} é {invert_frase} ')
if frase == invert_frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

