from random import randint
import os
import ast


#FUNÇÃO DOS DADOS
def rolagem(dado):
    resultado = 0
    dado = dado.split('d')
    for i in range(int(dado[0])):
        resultado += randint(1, int(dado[-1]))
    return resultado