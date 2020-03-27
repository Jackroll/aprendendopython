import re #usado para retirar os caracteres especiais do cnpj

#sequencia multilicada pelos digitos do CNPJ para encontrar os digitos verificadores 1 e 2
REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):
    cnpj = apenas_numero(cnpj)                      #recebe o cnpj só com numero atraves da função apenas_numero()

    try:
        if num_repetidos(cnpj):                    #atraves da função num_repetidos verifica se se os nr são repetidos, se for retorna false
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj = cnpj, digito = 1)        # igual ao CNPJ digitado retira os 2 ultimos valores e adiciona 1º digito encontrado     
        novo_cnpj = calcula_digito(cnpj = novo_cnpj, digito = 2)   # igual ao CNPJ anteriro adicionado com o 2º digito encontrado
    except Exception as e:
        return False

    if novo_cnpj == cnpj:                                          #se o novo cnpj for igual ao CNPJ igual retorna true, caso contrário else
        return True
    else:                                   
        return False   

#Função para calcular os digitos verificadores
def calcula_digito(cnpj, digito):                   #recebe um nº de cnpj e um digito como parametro
    if digito == 1:                                 #se for digito 1, a sequencia multiplicadora começa a contar a partir do 2º valor ou seja 5
        regressivos = REGRESSIVOS[1:]               #guarda o valor na variável 'regressivos' a partir do 2º valor ou seja 5 [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        novo_cnpj = cnpj[:-2]                       #igual ao CNPJ original, retirados os dois ultimos valores, para em seguida adicionar o 1º digito encontrado
    elif digito == 2:                               #se for digito 2, a sequencia multiplicadora é usada integralmente
        regressivos = REGRESSIVOS                   #guarda o valor na variável 'regressivos' integralmente ou seja 5 [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        novo_cnpj = cnpj                            #igual ao CNPJ anterior, para em seguida adicionar o 2º digto encontrado
    else:
        return None

    total = 0                                           #cria uma variável para armazenar o valor total da multiplicação do cnpj pelo regressivos
    for indice, regressivo in enumerate(regressivos):   #indice usado para acessar o valo da posição do nº do cnpj para multiplicar pelo regressivo
        total += int(cnpj[indice]) * regressivo         #total armazena a soma da multiplicação entre o numero do cnpj pelo regressivo
        
    digito  = 11 - (total % 11)                         #configura o digito
    digito = digito if digito <= 9 else 0               # se o resultado da conta for maior ou igual a 9, o digito é ele mesmo , se senão o digito é 0

    return f'{novo_cnpj}{digito}'                       #inclui os digitos encontrados a variável que armazena o novo cnpj
    
#verifica se os numeros são repetidos
def num_repetidos(cnpj):
    sequencia = cnpj[0] * len(cnpj)             #multiplica o primeiro valor do cnpj pela a qtd de elementos se for igual ao cnpj informado confirma que é sequencia 

    if sequencia == cnpj:                       
        return True
    else:
        return False

#retira os caracteres do cnpj digitado
def apenas_numero(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)      
