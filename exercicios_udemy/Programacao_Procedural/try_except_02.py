# -*- encoding: utf-8 -*-
def valida (valor):
    try:
        valor = abs(int(valor))
        return valor
    except ValueError:
        pass
    except TypeError:
        pass

y = True
while y:
    numero = valida(input('Digite um numero :'))

    if numero is None :
        print('Não é numero')
    else:
        print(f'Agora sim : {numero*10}')
