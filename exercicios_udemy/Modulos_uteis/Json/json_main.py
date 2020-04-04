"""
trabalhando com json
Documentação : https://docs.python.org/3/library/json.html
json -> python = loads / load
python -> json = dumps / dump
"""

from aprendendopython.exercicios_udemy.Modulos_uteis.Json.dados import *
import json

# convertendo dicionário para json
dados_json = json.dumps(clientes_dicionario, indent =4)         #usado ident=4 para dar a correta identação
print(dados_json)

#convertendo de json para pyhton (dicionário)
print('xx'*50)
dicionario_json = json.loads(clientes_json)
for v,j in dicionario_json.items():
    print(v)
    print(j)

print('xx'*50)
#convertendo, criando e gravando um dicionário em json
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)
    print('Conversão efetuada !')

print('xx'*50)
#convertendo e lendo um json em dicionário
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)
for chave, valor in dados.items():
    print(chave)
    print(valor)