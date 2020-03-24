#tratando exceções


#O que for executado deve estar dentro do try
print('-='*50)
try:
    print(a)
# as mensagens de erro ou outras execussões devem ficar no except
except:
    print('Erro !!')

print('-='*50)
#O que for executado deve estar dentro do try
try:
    print(a)
# Tratando erro com o nome do erro e mostrando na tela
except NameError as erro:
    print('Erro !!', erro)

print('-='*50)
#O programa continua executando após o tratamento do erro
print('Programa continua executando ....')