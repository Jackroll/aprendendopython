# -*- coding: utf-8 -*-
"""
trabalhando com datas e horas
    -   strptime (str, formato) - recebe uma string e um formato
    -   .strftime (formato) - recebe um formato
    -   timestamp - calcula o timestamp de uma data informada
    -   fromtimestamp - cria uma data atrvés de um timestamp
    -   timedelta - efetuar calculos com datas
"""
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL            #Bibliotecas para passar datas para portugues
from calendar import mdays

#Passando a data para portugues
setlocale(LC_ALL, 'pt_BR.utf-8')

#data formato padrão - ano/mes/dia - hora:min:seg
data = datetime(2020, 4, 4, 0, 53, 20)
print(data)

print('-='*15)
#Diretivas para formatar as datas usando o método strftime, para dados já informadas como datas
data2 = data.strftime(('%d/%m/%Y %H:%M:%S'))        #data formatada conforme diretivas
print(data2)

print('-='*15)
#Criando datas sem formatação com o método strptime
data3 = datetime.strptime('20/02/2020', '%d/%m/%Y')
print(data3)

print('-='*15)
#A data tambem pode ser criada usando timestamp - o tempo em segundo de desde 1972
data4 = data.timestamp()    #econtrando o timestamp
print(data4)

data5 = datetime.fromtimestamp(1585972400.0)  #criando uma data por um timestamp
print(data5)

print('-='*15)
#Usando Timedelta, fazendo calculo com datas
data6 = datetime.strptime('23/02/1987 02:00:00','%d/%m/%Y %H:%M:%S')    #data criada e formatada
data6 = data6 + timedelta(days= 10, seconds= 50)                        #acrescido 10 dias e 50 segundos
print(data6)

print('-='*15)
#Diferença entre datas
d1 = datetime.strptime('23/02/1987 02:00:00','%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/02/1987 10:00:00','%d/%m/%Y %H:%M:%S')
dif = d2-d1
print(dif)                          #mostra a diferença completa
print(dif.seconds)                  #mostra a diferenã em segundos somente das horas
print(dif.total_seconds())          #mostra a diferenã em segundos dos dias e horas
print(dif.days)                     #mostra a diferenã dias
print(d1.time())                    #mostra só o tempo do d1

print('-='*15)
#Data atual e em portugues formatada
dt = datetime.now()
dt_format1 = dt.strftime('%A, %d de %B de %Y')
dt_format2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(dt_format1)
print(dt_format2)

print('-='*15)
#Verificando qtd de dias num mes
mes_atual = int(dt.strftime('%m'))
print(mes_atual, mdays[mes_atual])