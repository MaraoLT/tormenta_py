from .basicas import *
from .objetos_classes import *


def humano(personagem):
    '''
    Você se torna treinado em duas perícias a sua escolha (não precisam ser da sua classe). 
    Você pode trocar uma dessas perícias por um poder geral a sua escolha.
    '''
    # Versátil
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
    
    '''
    personagem.caracteristicas['Visão no Escuro'] = 'Você vê no escuro'
    personagem.caracteristicas['Conhecimento das Rochas'] = '+2 em testes de Percepção e Sobrevivência realizados no subterrâneo.'
    personagem.deslocamento = 6
    personagem.caracteristicas['Devagar e Sempre'] = 'Seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'
    personagem.PV.max += 3
    personagem.PV.extra_nivel['Duro como Pedra (anão)'] = 1
    personagem.caracteristicas['Tradição de Heredrimm'] = 'Você é perito nas armas tradicionais anãs. Para você, todos os machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.'
    # PROGRAMAR ISSO: Para você, todos os machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.


def dahllan(personagem):
    '''
    
    '''
    personagem.habilidades_poderes['Amiga das Plantas'] = 'Você pode lançar a magia Controlar Plantas (atributo-chave Sabedoria). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'
    personagem.habilidades_poderes['Armadura de Allihanna'] = 'Você pode gastar uma ação de movimento e 1 PM para transformar sua pele em casca de árvore, recebendo +2 na Defesa até o fim da cena.'
    personagem.caracteristicas['Empatia Selvagem'] = 'Você pode se comunicar com animais por meio de linguagem corporal e vocalizações. Você pode usar Adestramento para mudar atitude e persuasão com animais (veja Diplomacia, na página 118). Caso receba esta habilidade novamente, recebe +2 em Adestramento.'


def elfo(personagem):
    '''
    
    '''
    # Graça de Glórienn
    personagem.deslocamento = 12
    # Sangue Mágico
    personagem.PM.max += 1
    personagem.PM.extra_nivel['Sangue Mágico'] = 1
    # Sentidos Élficos
    personagem.caracteristicas['Visão na Penumbra'] = 'Você vê na penumbra.'
    personagem.pericias['Misticismo'].modificadores['Sentidos Élficos'] = 2
    personagem.pericias['Percepção'].modificadores['Sentidos Élficos'] = 2


def goblin(personagem):
    '''
    
    '''
    # Engenhoso

    # Espelunqueiro

    # Peste Esguia

    # Rato das Ruas


    


funcoes_racas = {
    'humano': humano,
    'anao': anao,
    'dahllan': dahllan,
    'elfo': elfo,
}