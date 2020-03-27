
import cnpj


cnpj1 = input('Digite um CNPJ : ')

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')