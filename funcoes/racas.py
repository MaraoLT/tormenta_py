from .basicas import *
from .objetos_classes import *


def humano(personagem):
    '''
    Você se torna treinado em duas perícias a sua escolha (não precisam ser da sua classe). 
    Você pode trocar uma dessas perícias por um poder geral a sua escolha.
    '''
    for i in range(2):
        if i == 0: print(f'A raça Humano lhe permite adquirir {2-i} perícias ou poderes. Quer uma perícia ou poder?')
        else: print(f'A raça Humano lhe permite adquirir {2-i} perícia ou poder. Quer uma perícia ou poder?')
        while True:
            resp = formatacao(input())
            if resp in 'pericia':
                # isso eh literalmente a função de escolher uma perícia
                pericia = escolhe_categoria(Palavra('perícia', 'perícias'), nomes_pericias, 1, personagem.pericias_treinadas())[0]
                personagem.adiciona_pericia(pericia)
                break
            elif resp in 'poder':
                # programar escolha de poder_geral
                # poder_geral = escolhe_categoria()
                print('Escolher um poder ainda não foi implementado :(')
                break
            else:
                print(f'{resp.title()} não é uma resposta válida. Tente novamente.')


def anao(personagem):
    '''
    Você recebe visão no escuro e +2 em testes de Percepção e Sobrevivência realizados no subterrâneo.
    '''



funcoes_racas = {
    'versatil': versatil
}