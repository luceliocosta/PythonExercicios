import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
print(year)
print(date)
print(currentDateTime)
ano = int(input('Digite o ano que nasceste: '))
idade = year - ano
print('Você tem {} anos de idade'.format(idade))
