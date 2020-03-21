#sistema de perguntas e respostas usando dicionário

#criado dicionário Perguntas que contem chave pergunta, e o valor da che é outro dicionário
#com perguntas e respostas
perguntas = {
    #{pk}     :       {pv}
    'pergunta 1' : {
        #{pv[pergunta]}
        'pergunta': 'Quanto é 2 + 2 ?',
        #{rk}       :   {rv}
        'respostas' : {'a': 1, 'b' : 4, 'c': 55},
        #{pv[resposta_certa]}
        'resposta_certa' : 'b'
    },
    'pergunta 2' : {
        'pergunta': 'Quanto é 2 * 10 ?',
        'respostas' : {'a': 20, 'b' : 350, 'c': 55},
        'resposta_certa' : 'a'
    },
    'pergunta 3' : {
        'pergunta': 'Quanto é 15 / 3 ?',
        'respostas' : {'a': 230, 'b' : 3, 'c': 5},
        'resposta_certa' : 'c'
    },
}

resposta_certa = 0                                  #variável para armazenar as respostas certas
for pk, pv in perguntas.items():                    #iteração para percorrer o dicionário pai
    print(f'{pk} : {pv["pergunta"]}')
    print('Respostas :')
    for rk, rv in pv['respostas'].items():          #iteraão para percorrer o dicionário filho
        print(f'[{rk}] : {rv}')
    resposta_usuario = input('Sua resposta : ')

    if resposta_usuario == pv['resposta_certa']:
        print('Acertou !! \n')
        resposta_certa += 1
    else:
        print('Errou !! \n')

qtd_perguntas = len(perguntas)
erros = qtd_perguntas - resposta_certa
percentual = int(resposta_certa / qtd_perguntas * 100)

print(f'Acertos: {resposta_certa}\nErros: {erros}\n{percentual} % de acerto')

