#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    #Desconto do IR:
    #Salário Bruto até 900 (inclusive) - isento
    #Salário Bruto até 1500 (inclusive) - desconto de 5%
    #Salário Bruto até 2500 (inclusive) - desconto de 10%
    #Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    # dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

from decimal import Decimal
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

horas = float (input('Digite o total de horas trabalhadas : '))
val_horas = float (input('Digite o valor da hora trabalhada : '))

sal_bruto = horas * val_horas

if sal_bruto <= 900 :
    ir = 0
    val_ir = 0
elif sal_bruto >900 and sal_bruto <= 1500 :
    ir = 5/100
    
elif sal_bruto >1500 and sal_bruto <= 2500 :
    ir = 10/100
    
else :
    ir = 20/100
    
val_ir = sal_bruto * ir

inss = 10/100
fgts = 11/100
total_descontos = (sal_bruto*ir) + (sal_bruto*inss)

print('Salário Bruto: ({:.0f} * {:.0f}) {:>20} R$ {:>8.02f}'.format(horas, val_horas,':', sal_bruto))
print('(-) IR ({:.0f} %) {:<30} : R$ {:>8,.02f}'.format(ir*100, '',val_ir ))
print('(-) INSS ({:.0f} %) {:>29} R$ {:>8,.02f}'.format(inss*100,':',sal_bruto*inss))
print('FGTS ({:.0f} %) {:>33} R$ {:>8,.02f}'.format(fgts*100,':',sal_bruto*fgts))
print('Total de descontos {:>26} R$ {:>8,.02f}'.format(':', total_descontos))
print('Salário liquido {:>29} R$ {:>8,.02f}'.format(':',sal_bruto-total_descontos ))