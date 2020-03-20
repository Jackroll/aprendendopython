

variavel = 'valor'                  #variável de escopo global (não é boa prática) acessivel no escopo de qualquer função, no entanto não consigo mudar seu valor

def func():
    outra_variavel = 'texto'        #variável de escopo local, não acessível em outra variável
    return outra_variavel           #retornando a variável criada no escopo local

def func_2(arg):                    #função 2 com 1 argumento
    print(arg)


var = func()                        #atribuindo a função a uma variável, deste modo posso usar suas variáveis em outra função

func_2(var)                         #acessando a variável em outra função através da criação de uma variavel e argumento