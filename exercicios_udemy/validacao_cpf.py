"""
061.119.009-51
"""

#cpf = [0,6,1,1,1,9,0,0,9,5,1]
cpf = [1,6,8,9,9,5,3,5,0,0,9]
novo_cpf = []

k=0
l=0
for r,i in enumerate(range(10,1,-1)):
    k  += cpf[r] * i
    novo_cpf.append(cpf[r])

x = 11 - (k % 11)

if x > 9 :
    x = 0
    print('Digito 1 = 0')
else:
    x = x
    print(f'Digito 1 = {x}')

for r,i in enumerate(range(11,1,-1)):
    l  += cpf[r] * i
    #print(l)
    

y = 11 - (l % 11)

if y > 9 :
    y = 0
    print('Digito 2 = 0')
else:
    y = y
    print(f'Digito 2 = {y}')

novo_cpf.append(x)
novo_cpf.append(y)

if novo_cpf == cpf:
    print('CPF válido')
else :
    print('CPF inválido')
