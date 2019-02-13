# -*- coding: utf-8 -*-

# imports
import random

# Criando uma lista de enforcamento do boneco
forca = [
    '''
    +----- +
    |      |
    0      |
           |
           |
           |
    ''',
    '''
    +----- +
    |      |
    0      |
    |      |
           |
           |
    ''',
    '''
    +----- +
    |      |
    0      |
   /|      |
           |
           |
    ''',
    '''
    +----- +
    |      |
    0      |
   /|\     |
           |
           |
    ''',
    '''
    +----- +
    |      |
    0      |
   /|\     |
   /       |
           |
    ''',
    '''
    +----- +
    |      |
    0      |
   /|\     |
   / \     |
           |
    '''
]
erros = 0
acertos = []
# Abrindo o arquivo com as palavras
arquivo = open("palavras.txt", "r")
# Escolhendo uma palavra de forma aleatória
palavra = random.choice(list(arquivo))
palavra = palavra.rstrip()
# Convertendo a palavra em uma lista de caracteres
letras = list(palavra)
# Dicionario das letras corretas com suas posições
ordenacao = {}
while erros <=5:
    escolha = input("Escolha uma letra ")
    if escolha in letras:
        if escolha not in acertos:
                acertos.append(escolha)
        else:
           print("Essa letra ja foi escolhida")
        # Posição da letra escolhida na palavra
        posicao=[i for i in range(len(letras)) if letras[i]==escolha]
        for pos in posicao:
            ordenacao.update({
                pos: '%s' %escolha
            })
        # Ordernação de acordo com o index da palavra
        ordenacao = (dict(sorted(ordenacao.items())))
        # Convertendo a palavra ordernada em uma lista
        palavra_lista = list(ordenacao.values())
        # Formando uma string da lista
        palavra_formada = ''.join(map(str, palavra_lista))
        if len(palavra_formada) == len(palavra):
            print("Você Ganhou")
            break
    else:
        print(forca[erros])
        erros += 1
if erros == 6:
    print("Você perdeu! A palavra escolhida foi: " + palavra)