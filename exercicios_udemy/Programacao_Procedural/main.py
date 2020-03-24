from pacotes.calculo_precos import aumento, desconto
from pacotes.formata import preco as formatacao #modulo preço importado com um apelido, para a variável preço não sobrescrever por ter o mesmo nome


preco = 50.00
preco_com_aumento = aumento(valor = preco, porcentagem =50, formata = True)
preco_com_desconto = desconto(valor = preco, porcentagem = 50, formata = True)

print(preco_com_aumento)
print(preco_com_desconto)

print(formatacao.real(100))