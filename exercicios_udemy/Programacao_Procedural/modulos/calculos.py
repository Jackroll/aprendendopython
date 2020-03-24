import math

PI = math.pi

def dobra_lista(lista):
    lista = [v *2 for v in lista]
    return lista

def multiplica(lista):
    v = 1
    for i in lista:
        v *= i
    return v





lista_numeros = [1,2,3,4,5]

if __name__ == "__main__":
    print(dobra_lista(lista_numeros))
    print(multiplica(lista_numeros))