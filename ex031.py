#DESAFIO 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual é a distância da viagem que deseja realiza em Km? '))
if dist < 200:
    preco = dist*0.5
    #print(' A sua passagem custa $R{:.2f}'.format(preco))
else:
    preconovo = dist*0.45
print('A sua passagem custa $R{:.2f}'.format(preconovo))
print('OBRIGADO! Tenha uma boa viagem!')