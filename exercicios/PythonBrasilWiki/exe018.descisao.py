#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
# meses com 30 dias: 4 (abril), 6 (junho), 9 (Setembro), 11 (Novembro)
# meses com 31 dias : 1 (janeiro), 3 (março), 5 (maio), 7 (julho), 8 (agosto), 10 (outubro), 12 (dezembro)
# 29 Fevereiro quando bissexto
# 28 fevereiro quando não bissexto
# Exemplo: 30/01/2020 - Data valida
# Exemplo: 31/04/2020 - Data invalida
from datetime import date, datetime


data = input('Informe uma data (dd/mm/aaaa) : ')

data_str = datetime.strptime(data, '%d/%m/%y')

lista_trinta = [4,6,9,11]

print(data_str)