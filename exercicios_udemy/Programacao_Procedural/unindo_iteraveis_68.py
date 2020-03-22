#unindo iteráveis usando zip e zip_longest

#usando ZIP, une pela menor lista
cidades = ['São Paulo', 'Floripa', 'Poa', 'BH']
estados = ['SP', 'SC', 'RGS']

cidades_estados = zip(cidades, estados)         #deve ser feito um for para acessar os valores que foram unidos
print(list(cidades_estados))                    #uma opção é transformar em list para visualizar

cidades_estados1 = zip(cidades, estados) 
for valor in cidades_estados1:                   #acessando os valores através do for
    print(valor)

#usando zip_longest
from itertools import zip_longest
cidades_estados2 = zip_longest(cidades, estados, fillvalue='Estado')        #inclui os valores que sobram da maior lista e incluem none, ou valor padrão atraves do fillvalue
print(list(cidades_estados2))