"""
CSV - coma separated values - arquivos separados por vírgulas
Usado no excel, googlew sheets, bases de dados, clientes de e-mail etc...
"""
import csv
# abrindo e lendo o conteudo do arquivo
with open('clientes.csv','r') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)                             # pula a primeira linha

    for v in dados:
        print (v)

print(':::'*50)
# abrindo e convertendo o conteudo do arquivo para dicionário
with open('clientes.csv','r') as arquivo:
    dados = csv.DictReader(arquivo)

    for v in dados:
        print (v)

print(':::'*50)
# abrindo e convertendo o conteudo do arquivo para dicionário e acessando pelo valor da chave
with open('clientes.csv','r') as arquivo:
    dados = csv.DictReader(arquivo)

    for v in dados:
        print (v['Nome'])

print(':::'*50)
# abrindo e convertendo o conteudo do arquivo para dicionário e acessando pelo valor da chave
with open('clientes.csv','r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]             #usando list comprehension para armazenar a lista em uma váriável

# escrevendo em um novo arquivo.csv
with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )