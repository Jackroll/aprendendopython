from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

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
