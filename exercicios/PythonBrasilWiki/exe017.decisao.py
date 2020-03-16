#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
#Se dividido por 4 com resto = 0 e divisivel por 400 com resto = 0

ano = int(input('Informe o ano : '))

if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print('Ano Bissexto')
else :
    print('Ano não bissexto')