#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

periodo = str(input('Qual turno você estuda : M - Matutino, V-Vespertino, N-Noturno : '))
periodo_upper = periodo.upper()

if periodo_upper == 'M' :
    print("Turno Matutino")
elif periodo_upper == 'V' :
    print("Turno Vespertino")
elif periodo_upper == 'N' :
    print('Turno Noturno')
else :
    print('Opção invalida')