from pacotes.formata import preco

def aumento(valor, porcentagem, formata = False):
    r = valor * (1 + (porcentagem/100))
    
    if formata:
        return preco.real(r)
    else:
        return r


def desconto(valor, porcentagem, formata = False):
    r = valor * (1 - (porcentagem/100))
    if formata:
        return preco.real(r)
    else:
        return r
