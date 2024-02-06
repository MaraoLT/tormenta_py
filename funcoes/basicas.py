from dataclasses import dataclass, field
from random import randint
import os
import ast
import unicodedata

# paths
path = '/home/maraolt/Documents/projects/automatic_rpg_battles' # ubuntu desktop/notebook

def rolagem(dado):
    resultado = 0
    dado = dado.split('d')
    for i in range(int(dado[0])):
        resultado += randint(1, int(dado[-1]))
    return resultado


def erro():
    print('Erro, tente novamente!')


def abre_arquivo(nome_arquivo):
    with open(os.path.join(path+'/informacoes', nome_arquivo)) as arquivo:
            try:
                nomes_categoria = ast.literal_eval(arquivo.readline())
            except ValueError:
                print("malformed string; skipping this line")
            except SyntaxError:
                print("looks like some encoding errors with this file...")
            linhas = arquivo.readlines()

    return nomes_categoria, linhas


def remove_acentos(original):
    processamento = unicodedata.normalize("NFD", original)
    processamento = processamento.encode("ascii", "ignore")
    processamento = processamento.decode("utf-8")

    return processamento


def formatacao(texto):
    return remove_acentos(texto.lower().strip())


def escolhe_categoria(categoria, nomes_categoria, n_escolhas = 1, escolhidos_antes = [], genero = 0):
    i = 0
    escolhidos = []
    while i < n_escolhas:
        print(f'\nEscolha {n_escolhas-i} ', end='')
        if n_escolhas > 1: print(f'{categoria.plural} dentre: ')
        else: print(f'{categoria.singular} dentre: ')
        for nome_categoria in nomes_categoria:
            if nome_categoria not in escolhidos and nome_categoria not in escolhidos_antes:
                print(f'-{nome_categoria.title()}')
        item_escolhido = formatacao(input())
        encontrou = False
        for nome_categoria in nomes_categoria:
            if item_escolhido in formatacao(nome_categoria):
                if nome_categoria not in escolhidos and nome_categoria not in escolhidos_antes:
                    escolhidos.append(nome_categoria)
                    i += 1
                    if genero: print(f'{categoria.singular.title()} escolhido: {nome_categoria.title()}')
                    else: print(f'{categoria.singular.title()} escolhida: {nome_categoria.title()}')
                    encontrou = True
                    break
                else:
                    print(f'{nome_categoria.title()} já foi escolhido!')
                    encontrou = True
                    break
        if not encontrou:
            print(f'{item_escolhido.title()} não é um item válido!')

    return escolhidos
