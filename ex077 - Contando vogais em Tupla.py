# DESAFIO 077
#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
           'Mercado', 'Programador', 'Futuro')
for palavra in palavras:
    #print(palavra)
    print(f'\nNa palavra {palavra} temos: ', end=' ')
    for vogal in range(len(palavra)):
        if palavra[vogal].lower() in 'aeiou':
            print(palavra[vogal].lower(), end=' ')

        #if palavra[vogal].lower() == 'a':
            #print('a', end=' ')
        # elif palavra[vogal].lower() == 'e':
        #     print('e', end=' ')
        # elif palavra[vogal].lower() == 'i':
        #  print('i', end=' ')
        # elif palavra[vogal].lower() == 'o':
        #     print('o', end=' ')
        # elif palavra[vogal].lower() == 'u':
        #     print('u', end=' ')




