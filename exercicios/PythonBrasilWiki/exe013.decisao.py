#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

dia = input('Digite um numero do dia da semana :')              

semana = {'1':'Domingo', '2':'Segunda', '3' : 'Terça', '4':'Quarta', '5':'Quinta', '6':'Sexta', '7':'Sabado'}  #Cria um dicionário com os dias da semana

print(semana.get(dia, 'Valor inválido')) # Busca o dia da semana conforme o valor digitado, se não existir mostra o valor padrão do get