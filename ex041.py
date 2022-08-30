#DESAFIO 41
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
ano_actual = date.today().year
ano_nasc = int(input('Em que ano nasceste? '))
idade = ano_actual - ano_nasc
print(f'Você têm {idade} anos de idade')
if idade <= 9:
    print('De acordo com a sua idade você pertence a categoria MIRIM')
elif idade <= 14:
    print('De acordo com a sua idade você pertence a categoria INFANTIL')
elif idade <= 19:
    print('De acordo cm a sua idade você pertence a categoria JÚNIOR')
elif idade <= 25:
    print('De acordo com a sua idade você pertence a categoria SÊNIOR')
else:
    print('De acordo com a sua idade você pertence a categoria MASTER')