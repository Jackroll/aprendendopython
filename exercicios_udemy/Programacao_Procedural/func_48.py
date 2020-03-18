def Ola(nome, saudacao):
    print(nome, saudacao)

Ola('ola', 'jacson')

print()
print(' Exercicio 2 -------------')

def soma(a,b,c):
    somatorio = a+b+c
    print(somatorio)
soma(2,2,2)

print()
print(' Exercicio 3 -------------')

def perc (x, y):
    return (x*(1+(y/100)))

print(perc(50,10))

print()
print(' Exercicio 4 -------------')

def FizzBuzz (x):
    if (x % 5) == 0 and (x % 3) == 0:
        return 'FizzBuzz'
    if x % 2 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return x

print(FizzBuzz(9))