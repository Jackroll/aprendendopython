#Solicita dois numeros e imprimi o maior

n1 = float(input('Digite o primeiro nº inteiro: '))
n2 = float(input('Digite o segundo nº inteiro: '))

if n1 > n2 :
    print(f'{n1} é maior que {n2}')
else :
    print(f'{n2} é maior que {n1}')