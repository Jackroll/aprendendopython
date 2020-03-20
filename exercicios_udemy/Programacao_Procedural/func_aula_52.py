


# *args = quando não sei quantos argumentos vai ter a função
# **kwargs = (key words args) argumentos nomeados

def func(*args, **kwargs):
    print(args, kwargs)

    idade = kwargs.get('idade')             #maneira de acessar o argumento da função indiretamente, get utilizado quando não sabemos se o argumento existe
    print(idade)

lista = [1,2,3]
lista2 = [10,20,30]


func(lista, lista2)                         # Mostra tupla de listas e dicionáro vazio não atribuido do **kwargs
func(lista, lista2, nome = 'Jacson')        # Mostra tupla de listas e dicionáro do **kwargs
func(*lista, *lista2, nome = 'Jacson')      # Desempacota as listas mostrando em tupals e dicionáro do **kwargs
func(*lista, *lista2, idade = 30)           # Desempacota as listas mostrando em tupals e dicionáro do **kwargs



#print(type(func()))