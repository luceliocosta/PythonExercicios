#DESAFIO 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoactual = date.today().year
ano_nasc = int(input('Qual foi o ano que nasceste? '))
idade = anoactual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos de idade em {anoactual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado há  {idade - 18} anos')
    print(f'Seu alistamento foi em {anoactual - (idade - 18)}')
elif idade < 18:
    print(f'Ainda faltam {18 -idade} anos para você se alistar para o serviço militar.')
    print(f'Seu alistamento será em {anoactual + (18 - idade)}.')
else:
    print('É a hora exata para você se alistar ao serviço militar')

