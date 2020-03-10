#Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    #Dicas:
    #Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    #Triângulo Equilátero: três lados iguais;
    #Triângulo Isósceles: quaisquer dois lados iguais;
    #Triângulo Escaleno: três lados diferentes; 

ladoA = float(input("Informe o comprimento do Lado A :"))
ladoB = float(input("Informe o comprimento do Lado B :"))
ladoC = float(input("Informe o comprimento do Lado C :"))

AB = ladoA + ladoB
AC = ladoA + ladoC
BC = ladoB + ladoC

if (abs(ladoA - ladoB) < ladoC < AB) or (abs(ladoA - ladoC) < ladoB <AC) or (abs(ladoB - ladoC) < ladoA < BC) :
    forma = True
else :
    forma = False

if (forma):
    if (ladoA == ladoB) and (ladoB == ladoC):
        triangulo = 'Equilátero'
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        triangulo = 'Isósceles'
    else :
        triangulo = 'Escaleno'
    print(f'Triangulo : {triangulo}')
else :
    print('Não é triangulo')
            


