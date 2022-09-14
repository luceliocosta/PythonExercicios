#DESAFIO 062
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos.
"""
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
an = a1
nosvostermos = 1
contador = 1

while contador < 11:
    print('{} -> '.format(an), end='')
    an = an + r

    contador = contador + 1
    totaltermos = int(contador - 1)

    if contador == 11:
        print('PAUSE')
        while nosvostermos != 0:
            nosvostermos = int(input('Quantos termos você quer mostrar mais? '))
            auxcontador = 1
            totaltermos = totaltermos + nosvostermos
            while auxcontador <= nosvostermos:
                print('{} -> '.format(an), end='')
                an = an + r
                auxcontador = auxcontador + 1
            if nosvostermos != 0:
                print('PAUSE')

print('Progressão finalizada com {} termosmos trados'.format(totaltermos))

"""
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
an = a1
novostermos = 10
contadortermos = 1
total = 0


while novostermos != 0:
    total = total + novostermos
    while contadortermos <= total:
        print('{} -> '.format(an), end='')
        an = an + r
        contadortermos = contadortermos + 1
    print('Pause')
    novostermos = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termosmos trados'.format(total))

