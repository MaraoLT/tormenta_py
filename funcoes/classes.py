from .basicas import *
from .objetos_classes import *

# # Arcanista
def arcanista(personagem):
    '''
    
    '''
    for i in range(personagem.nivel):
        for habilidade in personagem.classe.habilidades:
            




    funcoes_por_nivel = {i: globals()[f'arcanista_{i}'] for i in range(1, 21)}

    for i in range(1, personagem.nivel + 1):
        funcao = funcoes_por_nivel.get(i)
        if funcao: funcao()