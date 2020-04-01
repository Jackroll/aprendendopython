#método 02 de criar gerenciador de contexto - usando contextmanager, atraves da criação de uma função.

from contextlib import contextmanager

# é criado uma função normal, só que decorada com @contextmanager para virar gerenciador de contexto
@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(arquivo, modo)           #abre o arquivo
        yield arquivo                           # é igual o return, só que ao contrário do return, executa o código seguinte
    finally:
        arquivo.close()                         #fecha o arquivo

with abrir('teste_02.txt', 'w') as arquivo:     #para funcionar deve sempre ser usado com o with
    arquivo.write('linha 01 \n')
    arquivo.write('linha 02 \n')
    arquivo.write('linha 03 \n')
    arquivo.write('linha 04 \n')