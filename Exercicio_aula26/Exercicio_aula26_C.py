nome = str(input('Informe seu primeiro Nome: '))
qtd_letras = len(nome)

if qtd_letras > 6 :
    print('Nome grande')
elif qtd_letras >=5:
    print('Nome médio')
else:
    print('Nome curto')