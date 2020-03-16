from datetime import datetime

nome = str(input('Informe o nome: '))
idade = int(input('Informe a idade: '))
altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso : '))
imc = round(peso/(altura*altura),2)
ano_atual = int(datetime.strftime(datetime.now(), '%Y')) 
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} Kg\nO IMC de {nome} é {imc}\n{nome} nasceu em {ano_nascimento}')