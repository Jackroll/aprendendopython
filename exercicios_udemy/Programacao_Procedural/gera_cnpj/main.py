import gera_cnpj
from random import randint

cnpj = str((randint(10000000, 99999999))) + '0001' #gera os 8 primritos digitos do CNPJ + 0001


gera_cnpj.valida(cnpj)
    

