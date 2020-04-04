# -*- coding: utf-8 -*-
"""
Trabalhando com arquivos
 - deve ser informado o caminho(diretório) para a busca
 - e o termo (nome do arquivo) para a buscar, se não informar o nome do arquivo retorna todos os arquivos do diretório
"""
import os # Biblioteca para trabalhar com arquivos

# Função para formatar o tamanho dos arquivos
def formata(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto ='B'
    elif tamanho <mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho <giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho <tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.',',')


caminho_procura = input('Digite um caminho: ')                      #caminho que deve ser feita a busca
termo_procura = input('Digite um termo para fazer a busca:')        # valor a buscar

# variáveis que armazenam o total de arquivo e tamanho total dos arquivos encontrados
conta = 0
tamanho_total = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):                 # método que faz a busca no caminho informado
    for arquivo in arquivos:                                                # percorrer todos os arquivos nos arquivos do caminho informado
        if termo_procura in arquivo:                                        # busca o ermo nos arquivos
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)              # os.path.join junta o caminho + o nome do arquivo
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)       # os.path.splitext inclui a extensão ao nome do arquivo
                tamanho = os.path.getsize(caminho_completo)                 # os.path.getsize pega o tamanho dor arquivo encontrado

                print('-='*30)
                print('Arquivo encontrado: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho, 'bytes')
                print('Tamanho formatado: ', formata(tamanho))              # chamada a função para formatar o tamanho do arquivo
                tamanho_total += tamanho
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não econtrado.')
            except Exception as e:
                print('erro desconhecido', e)

print(':'*40)

print(f'{conta} arquivo(s) encontrados !')          #mostra o total dos arquivos encontrados
print(f'Total : {formata(tamanho_total)}')          # mostra o total do tamanho dos arquivos encontrados





