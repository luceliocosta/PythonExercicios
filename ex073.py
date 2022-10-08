# DESAFIO 073
#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético Mineiro', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goianiense')
print('Lista de times do Brasileirão 2017: {}'.format(times))
print('=-'*40)
print(f'Os primeiros 5 times: {times[:5]}')
print('=-'*40)
print(f'Os últimos colocados: {times[-4:]}')
print('=-'*40)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('=-'*40)
print(f'O time Chapecoense encontra-se na {times.index("Chapecoense") + 1}ª posição')


