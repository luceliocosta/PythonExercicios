#DESAFIO 40
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a sua primeira nota :'))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
if m > 7:
    print(f'\033[32mO aluno está APROVADO com média de {m}')
elif m < 5:
    print(f'\033[31mO aluno está REPROVADO com média de {m}')
else:
    print(f'\033[33mOaluno está em RECUPERAÇÃO com média de {m}')