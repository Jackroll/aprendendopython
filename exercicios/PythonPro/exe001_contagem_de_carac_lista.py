#Ordenando os caracteres de uma palavra (lista) e mostrando as quantidades de cada letra

def contar_caracteres(s):                               #função para contar valores ordenados

    """Função que conta os caracteres de uma string
    Ex:

    >>> contar_caracteres('banana')
    a : 3
    b : 1
    n : 2
    """    

    carac_ordenados = sorted(s)                         #Ordena as letras da palavra em ordem alfabética
    carac_anterior = carac_ordenados[0]                 #atribui a uma variável o caracter da primeira posição
    contagem = 1

    for caracter in carac_ordenados [1:]:               #percorre a lista a partir do resultado 1, pois o 0 já foi atribuido na variável caracter_anterior
        if caracter == carac_anterior:
            contagem += 1                               #se ao percorre a lista o caracter for igual ao anterior incrementa a variável contagem, caso contrario mantem em 1
        else:
            print( f'{carac_anterior} : {contagem}')    #Se não houver caractere repetido imprime o caracter e a contagem
            carac_anterior = caracter                   #a variavel de comparação passa a ter o valor da variável que percorre a lista, para poder comparar na próxima iteração
            contagem = 1                                #Se não há repetição do caracter então a contagem = 1
            
    print(f'{carac_anterior} : {contagem}')             #Mostra na tela o caracter e quantidade de repetição deste
    

if __name__ == "__main__":                              #Usado para caso a função seja importado em outro arquivo, não seja mostrado o resultado dos códigos de teste abaixo.
    nome = str(input('Digite uma palavra :'))           #Solicita que seja digitado uma palavra, que será atribuida a variável nome
    print(nome)                                         #mostra a palavra digitada na tela
    contar_caracteres(nome)                             #executa a função para a palavra digitada.