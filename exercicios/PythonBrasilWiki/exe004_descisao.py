#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

letra = str(input('Digite uma letra :'))
letra_upper = letra.upper()                  #transforma a string para Uppercase para não haver erro em caso de digitação da letra em minusculo

vogais = ['A', 'E', 'I', 'O', 'U']           #cria uma lista com as vogais

if letra_upper in vogais:                    #se o valor digitado estiver contido na lista é uma vogal caso contrário é consoante
    print(f'{letra_upper} é vogal')
else:
    print(f'{letra_upper} é consoante')