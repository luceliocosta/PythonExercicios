print('='*40)
print('{:^40}'.format('MULTIBANCO [MB]'))
print('='*40)

valor = int(input('Que Valor você quer levantar? R$'))
total = valor
total_notas = 0
nota = 50
while True:
    if total >= nota:
        total = total - nota
        total_notas = total_notas + 1
    else:
        if total_notas != 0:
            print('Total de {} notas de R${}'.format(total_notas, nota))
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_notas = 0

        if total == 0:
            break
print('=' * 40)
print('Volte Sempre ao Banco Costa! Tenha um excelente dia!')




