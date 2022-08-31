#DESAFIO 055
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
homem_maisvelho = 0
mulherMenosDe20 = 0

for x in range(1, 5):
    print(f'------ {x}ª Pessoa ------')
    nome = str(input('Digite seu nome: ')).capitalize()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media = media + idade
    if sexo =='F' and idade < 20:
        mulherMenosDe20 += 1
    if idade > homem_maisvelho:
        homem_maisvelho = idade
        nomeHomemMaisVelho = nome
mediagrupo = media/x
print('A média de idade do grupo é de {}'.format(mediagrupo))
print('O homem mais velho tem {} e se chama {}'.format(homem_maisvelho, nomeHomemMaisVelho))
print(f'Ao todo são {mulherMenosDe20} mulheres com menos de 20 anos')
