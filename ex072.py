# DESAFIO 072
#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

tupla_número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

número = int(input('Digite um número entre 0 a 20: '))
while número > 20 or número < 0:
    número = int(input('Tente novamente. Digite um número entre 0 a 20:  '))
print(f'Você digitou o número {tupla_número[número]}.')
