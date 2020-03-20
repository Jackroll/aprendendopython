#função anonima é conhecida como função lambida, ela não tem nome nem return
#passar uma função para outra função, ou passar parametros para outra função

"""#Função nomeada normal
def func (arg, arg2):
    return(arg*arg2)

var = func (2,2)
print(var)

-----------------------------------------------------------
#Função Lambda - anonima igual a anterior resolvida em 2 linhas
a = lambda arg, arg2: arg*arg2
print(a(2,2))
"""

#exemplo de uso prático da função lambda

lista = [
   #[0]    [1]
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

"""#Se quiser ordenar a lista pelo numero do item [0] ou [1]
#tem que ser criada uma função que retorne o item desejado
#e chamar a função detro da função sort

def func(item):                         #Função para retornar o numero da lista [1]
    return item[1]

lista.sort(key=func, )      #ordena a lista conforme o numero retornado pela função [1] = preços
print(lista)"""

#Ordenando a mesma lista usando a expressão lambda

lista.sort(key=lambda item:item[1]) 
print(lista)

#outro jeito usando sorted

print(sorted(lista, key=lambda i:i[1]))