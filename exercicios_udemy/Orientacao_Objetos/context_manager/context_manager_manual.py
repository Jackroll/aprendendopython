#método 01 de criar gerenciado de contexto - manualmente atraves da criação de uma classe
#usando o método __enter__ e o __exit__

"""# Criando, abrindo e escrevendo em um arquivo, usando o with open não precisa fechar o arquivo
with open('teste.txt', 'w') as arquivo:
    arquivo.write('escreveando algo')"""

#Criando um gerenciador de contexto, deste modo a classe Arquivo, abre, retorna e fecha o arquivo automaticamente
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo o arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando o arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo')
        return self.arquivo.close()


with Arquivo('teste.txt', 'w') as arquivo:      #para funcionar deve sempre ser usado com o with
    arquivo.write('escreveando algo')