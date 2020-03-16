from cliente import Cliente, Endereco


cliente1 = Cliente('jacson', 32)
cliente1.insere_endereco('Imarui', 'SC')
cliente1.mostra_cliente()
print('-------------------------')
cliente2 = Cliente('João', 90)
cliente2.insere_endereco('Imarui', 'SC')
cliente2.mostra_cliente()
print('-------------------------')
cliente3 = Cliente('Inês Maria', 2)
cliente3.insere_endereco('Imarui', 'SC')
cliente3.mostra_cliente()