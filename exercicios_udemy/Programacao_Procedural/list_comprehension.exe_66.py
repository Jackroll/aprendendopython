#fazer a soma dos valores de produtos de uma lista usando list comprehension

carrinho = [
        #(v1)    (v2)
    ('Produto 1', 30),
    ('Produto 2', 20),
    ('Produto 3', 50),
]


#Executando com for 
"""total = 0
for v in carrinho:
    total += v[1]

print(total)"""

#executando pela list comprehension
total = sum([float(v2) for v1, v2 in carrinho])     #para v1, v2 pega o v2 do carrinho e faz a soma (sum)
print(total)