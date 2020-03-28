"""
Encapsulamnento
Convensão:
_ Protected (1 underline em frente a variável, atributo ou método) recomenda-se que não se acesse a variável de fora da classe
__ Private (2 underlines em frente a variável, atributo ou método) recomenda-se fortemente que não se acesse a variável de fora da classe
Private pode ser acessado, ou modificar o seu valor (_nomeclasse__nomeatributo)
"""

class BaseDeDados():
    def __init__(self):
        self._dados = {}

    def inserir_dados(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id : nome}
        else:
            self._dados['clientes'].update({id : nome})
    
    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id] 



bd = BaseDeDados()
bd.inserir_dados(1 , 'Jacson')
bd.inserir_dados(2, 'John')
bd.inserir_dados(3, 'Lucas')

bd.lista_clientes()
print('-='*30)
bd.apaga_cliente(2)

bd.lista_clientes()

#atravez da instancia do objeto foi possível acessar um atributo de classe e mudar seu valor 
# fazendo com que o código passe a não funcionar mais corretamente
# Exemplo abaixo
print('-='*30)
#bd._dados = 'exemplo de acesso a um atributo de classe público, que vai quebrar o código inteiro' 


print('-='*30)
bd.lista_clientes()



