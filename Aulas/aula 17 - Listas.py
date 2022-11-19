"""
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 7 in num:
    num.remove(7)
else:
    print('Não achei o número 7')
#num.remove(4)
#num.pop(0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
"""
"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont + 1}º valor: ')))

for index, val in enumerate(valores):
    print(f'Na posição {index + 1} encontrei o {val}')
print('Final da lista')
"""

"""
a = [2, 3, 4, 7]
b = a[:]
c = b[:]
b[2] = 100

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')

"""
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

df_teste = df
df_teste.insert(2, "city", ['Lahore', 'Dehli', 'New York'], True)
#print(data)
print(df)
print(df_teste)

