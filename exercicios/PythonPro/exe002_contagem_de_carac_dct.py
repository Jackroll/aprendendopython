#Ordenando os caracteres de uma palavra e colocando em um dicionário

def contar_caracteres(s):                               #função para contar valores ordenados

    """Função que conta os caracteres de uma string e insere em um dicionário
    Ex:

    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n':2}

    :param s: string a ser contada

    """    

    resultado = {}                                      #Cria um dicionário para inclusão dos carcteres e seus valores de contagem

    for caracter in s:                                  #percorre cada caractere presente na string S  
        contagem = resultado.get(caracter,0)            #armazena na variável contagem a posição do caracter, se ele não existir ainda como por exemplo na prmeira iteração,
                                                        #o valor a contagem é igual a, valor default será 0, passado atraves do get
        contagem+=1                                     #incrementa o valor da contagem
        resultado[caracter] = contagem                  #inclui no dicionário resultado, o caracter e a contagem feita
    
    return resultado                                    #retorna o dicionário com os valores
    

if __name__ == "__main__":                              #Usado para caso a função seja importado em outro arquivo, não seja mostrado o resultado dos códigos de teste abaixo.
    nome = str(input('Digite uma palavra :'))           #Solicita que seja digitado uma palavra, que será atribuida a variável nome
    print(nome)                                         #mostra a palavra digitada na tela
    print(contar_caracteres(nome))                      #executa a função para a palavra digitada e mostra os valores do dicionario
    