from pacotes.calculo_precos import aumento, desconto
from pacotes.formata import preco


preco = 50.00
preco_com_aumento = aumento(valor = preco, porcentagem =50, formata = True)
preco_com_desconto = desconto(valor = preco, porcentagem = 50, formata = True)

print(preco_com_aumento)
print(preco_com_desconto)