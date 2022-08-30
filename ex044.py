#DESAFIO 44
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJAS COSTA'))
preconormal = float(input('Qual é o preço normal do produto(R$): '))
print('''FORMAS DE PAGAMENTO
[0]- À vista dinheiro/cheque
[1]- À vista no cartão
[2]- Em até 2x no cartão
[3]- 3X ou mais no cartão
''')
opcao = int(input('Sua opção: '))
if opcao == 0:
    preconormal = preconormal - preconormal*0.1
    print('O valor a ser pago pelo produto é igual a R${:.2f}'.format(preconormal))
elif opcao == 1:
    preconormal = preconormal - preconormal*0.05
    print('O valor a ser pago pelo produto é igual a R${:.2f}'.format(preconormal))
elif opcao == 2:
    parcela = preconormal/2
    print('O valor a ser pago pelo produto é igual a R${:.2f}'.format(preconormal))
    print('Sua compra será parcelada {}x de R${} SEM JUROS'.format(parcela, preconormal))
else:
    parcela = int(input('Quantas parcelas?'))
    div = (preconormal*1.2)/parcela
    print('Sua compra será parcelada {}x de R${:.2f} COM JUROS'.format(parcela, div))
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preconormal, preconormal*1.2 ))



