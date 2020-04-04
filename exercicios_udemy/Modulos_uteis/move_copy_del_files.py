# -*- coding: utf-8 -*-
"""
caminhando nos diretório, Copiando, movendo e removendo arquivos.
os.walk - caminha no diretório informado
shutil.copy - copia arquivos de um diretório para outro
shutil.move - move um arquivo de um diretório para o outro
os.remove - deleta arquivos de um diretório
os.mkdir - cria pasta em um diretório
"""
import os
import shutil           #biblioteca para copiar, mover, remover arquivos

caminho_original = r'D:\Python\teste'   #diretórios
caminho_novo = r'D:\Python\teste1'

try:
    os.mkdir(caminho_novo)                                  #cria uma nova pasta em um diretório
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe !')

for root, dirs, files in os.walk(caminho_original):         #percorre o diretório com os.walk
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #copiando arquivos xlsx de uma pasta para a outra
        if '.xlsx' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso !')

        #removendo arquivos xlsx de uma pasta para a outra
        if 'xlsx' in file:
            os.remove(old_file_path)
            print(f'Arquivo {file} removido com sucesso.')

        # movendo arquivos txt de uma pasta para a outra
        if 'txt' in file:
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso !')