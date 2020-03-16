from pythonbirds.oo.Associacao.classes import Escritor
from pythonbirds.oo.Associacao.classes import Caneta
from pythonbirds.oo.Associacao.classes import MaquinaDeEscrever

#Criando objetos independentes - escritor / caneta / máquina
escritor = Escritor('João')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever()
print(maquina)

print('------------------------')

#criando associação entre as classes através da variável ferramenta da classe Escritor()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
