#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

letra = str(input('Digite F ou M :'))
letra_upper = letra.upper()         #transforma a string para Uppercase para não haver erro em caso de digitação da letra em minusculo


if letra_upper == 'F':
    print(f'{letra_upper} - é feminino')
elif letra_upper == 'M' :
    print(f'{letra_upper} - é masculino')
else :
    print ('Sexo invalido')