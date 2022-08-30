#DESAFIO 43
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu
# status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print('O seu IMC é igual a {:.2f}.'.format(IMC))
    print('Você está ABAIXO DO PESO NORMAL')

elif 18.5 <= IMC < 25:
    print('O seu IMC é igual a {:.2f}.'.format(IMC))
    print('Você está no PESO IDEAL')
elif 25 <= IMC < 30:
    print('O seu IMC é igual a {:.2f}'.format(IMC))
    print('Você já é considerado SOBREPESO')
elif 30 <= IMC < 40:
    print('O seu IMC éigual a {:.2f}'.format(IMC))
    print('Você já é considerado OBESO(a)')
else:
    print('O seu IMC é igual a {:.2f}'.format(IMC))
    print('Você está na OBESIDADE MÓRBIDA')
