"""1 - função 1 que recebe uma função 2 como parametro e retorne o valor da função 2 executada"""

def func1 (arg):
    return func2()

def func2():
    return 'Imprimindo valor da função 2 na função 1'
    

var = func1(func2)
print(var)

"""2 - crie uma função 1 wue recebe uma função2 como parametro e retorne o valor da função2 executada.
faça a função1 executar duas funções que recebem um numero diferente de argumentos"""


def mestre (funcao, *args, **kwargs):                   #função principal, recebe um argumento padrão 'função, e outros dois argumentos opcionais
    return funcao(*args, **kwargs)                      #argumentos opicionais repassagm argumentos de outras funções

def fala_oi (nome):
    return nome

def saudacao (nome, saudacao):
    return nome, saudacao

executando = mestre(fala_oi, 'Jacson')                  #executando a função fala_oi atravez da função mestre
executando2 = mestre(saudacao, 'Bom dia', 'Jacson')     # executando a função saudacao, atraves da função mestre
print(executando)
print(executando2)
    