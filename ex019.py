#DESAFIO 019
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Escreva o nome do terceiro aluno: ')
a4 = input ('Escreva o nome do quarto aluno: ')
list = [a1, a2, a3, a4]
x = choice(list)
print('O aluno escolhido foi {}'.format(x))