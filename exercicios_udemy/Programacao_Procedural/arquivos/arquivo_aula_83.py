

file = open('abc.txt', 'w+')        #cria o arquivo 'abc.txt' em modo de escrita w+ apaga tudo que ta no arquivo antes de iniciar a escrita
file.write('linha 1\n')             #escreve varias linhas no arquivo
file.write('linha 2\n')
file.write('linha 3\n')
file.write('linha 4\n')

print('-=' * 50)                    
file.seek(0,0)                      #coloca o cursor no inicio do arquivo para fazer a leitura
print('Lendo o arquivo :')
print(file.read())                  #faz a leitura do arquivo

print('-=' * 50)
file.seek(0, 0)                     #coloca o cursor no inicio do arquivo para fazer a leitura
print(file.readlines())             #gera uma lista com as linhas do arquivo

print('-=' * 50)
file.seek(0, 0) 
for linha in file.readlines():      #lendo atraves de um for
    print(linha, end='')            #end = '' retira a quebra de linha

file.close()                        #fecha o arquivo

print('-=' * 50)
with open ('abc2.txt', 'w+') as file:               #utilizando o with não precisar mandar fechar o arquivo com file.close()
    file.write('Arquivo 2 - linha 1\n')             #escreve varias linhas no arquivo
    file.write('Arquivo 2 - linha 2\n')
    file.write('Arquivo 2 - linha 3\n')
    file.write('Arquivo 2 - linha 4\n')

    file.seek(0)
    print(file.read())


print('-=' * 50)
with open ('abc3.txt', 'a+') as file:               #Adicionando linhas ao arquivo, o a+ manda o cursor para o final do arquivo
    file.write('Adcicionando linhas 1\n')
    file.write('Adcicionando linhas 2\n')
    file.write('Adcicionando linhas 3\n')
    file.write('Adcicionando linhas 4\n')
    file.write('Adcicionando linhas 5\n')
    file.seek(0)
    print(file.read())


print('-=' * 50)
with open ('abc3.txt', 'r+') as file:               #lendo oque esta dentro do arquivo e mostrando na tela atraves do r+
    print(file.read())