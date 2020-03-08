#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    #Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    #salários até R$ 280,00 (incluindo) : aumento de 20%
    #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    #o salário antes do reajuste;
    #o percentual de aumento aplicado;
    #o valor do aumento;
    #o novo salário, após o aumento. 

salario = float(input('Digite o valor do seu salario: '))
reaj_a = salario * 1.20
reaj_b = salario * 1.15
reaj_c = salario * 1.10
reaj_d = salario * 1.05

if salario <= 280 :
    print(f'Salario : {salario}, reajuste : 20%, valor do aumento : {salario * 0.20}, salario após reajuste: {reaj_a}')
elif salario > 280 and salario <= 700 :
    print(f'Salario : {salario}, reajuste : 15%, valor do aumento : {salario * 0.15}, salario após reajuste: {reaj_b}')
elif salario > 700 and salario <= 1500 :
    print(f'Salario : {salario}, reajuste : 10%, valor do aumento : {salario * 0.10}, salario após reajuste: {reaj_c}')
else :
    print(f'Salario : {salario}, reajuste : 5%, valor do aumento : {salario * 0.05}, salario após reajuste: {reaj_d}')