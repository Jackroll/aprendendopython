     if reverso < 2:                             #quando o reverso passar a ser menor que 2, reverso recebe o valor 11 para começar a 2º itereção
            reverso = 6
            d = 11 - (total % 11)                   #d armazena o resultado da conta 11 - (resto da divisão de total com 11)

            if d > 9:                               #se d for maior que 9, d = digito 1 = 0, caso contrario d = o próprio resultado da conta, d=d
                d = 0                               
            total = 0
            novo_cpf += str(d)  