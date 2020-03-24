#tratando erro de valor digitado

#Como o float sempre retorna uma string, para usar em um calculo deve ser convertido antes
#função para converter valor digitado em int ou float
def converte_numero(valor):
    try:
        valor = int(valor)          #primeiro tenta converter para inteiro, se der certo retorna o valor digitado em int
        return valor
    except ValueError:
        try:
            valor = float(valor)    #se falhar a primeira conversão tenta converter para float
            return valor
        except ValueError:          #se falhar a conversão anterior vai retornar o valor como None
            pass

while True:                         #executa o programa enquanto for True

    numero = converte_numero(input('Digite um numero: '))  #recebe o valor digitado

    if numero is None:                                      #se as conversões não derem certo, ou seja se for digitado letras
        print('Erro !!! Digite um numero.')                 #a função converte_numeros retorna None para valor, deste modo é solicitado 
                                                             #que digite um numero
    else:                                                  
        print(numero * 5)                                   #caso a conversão de certo é executado o calculo.