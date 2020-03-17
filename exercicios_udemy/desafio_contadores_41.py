"""fazer uma iteração para gerar a seguinte saída:
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
# método 01 - usando while
i = 0
j = 10
while i <= 8:
    print(i, j)
    i = i+1
    j = j-1

print('------------------')

# método 02 - usando for com enumerate e range

for r, i in enumerate(range(10,1, -1)):  #enumerate conta quantas vezes houve a iteração
    print(r, i)