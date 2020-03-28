"""Associação:
Relacionar classes independentes entre si
"""
from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Jacson")
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

print('-='*50)

escritor.ferramenta = caneta            #Associação atravéz do atributo ferramenta
escritor.ferramenta.escrever()

print('-='*50)
escritor.ferramenta = maquina            #Associação atravéz do atributo ferramenta
escritor.ferramenta.escrever()

