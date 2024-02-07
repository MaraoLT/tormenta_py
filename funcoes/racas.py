from .basicas import *
from .objetos_classes import *


def visao_escuro(personagem):
    personagem.caracteristicas.append(Habilidade('Visão no Escuro', 'Você vê no escuro.'))


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


# def anao(personagem):
#     '''
    
#     '''
#     personagem.caracteristicas['Visão no Escuro'] = 'Você vê no escuro'
#     personagem.caracteristicas['Conhecimento das Rochas'] = '+2 em testes de Percepção e Sobrevivência realizados no subterrâneo.'
#     personagem.deslocamento = 6
#     personagem.caracteristicas['Devagar e Sempre'] = 'Seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'
#     personagem.PV.max += 3
#     personagem.PV.extra_nivel['Duro como Pedra (anão)'] = 1
#     personagem.caracteristicas['Tradição de Heredrimm'] = 'Você é perito nas armas tradicionais anãs. Para você, todos os machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.'
#     personagem.proficiencias += ['Machado', 'Martelo', 'Marreta', 'Picareta']
#     # PROGRAMAR ISSO: Para você, todos os machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.


# def dahllan(personagem):
#     '''
    
#     '''
#     personagem.habilidades_poderes['Amiga das Plantas'] = 'Você pode lançar a magia Controlar Plantas (atributo-chave Sabedoria). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'
#     personagem.habilidades_poderes['Armadura de Allihanna'] = 'Você pode gastar uma ação de movimento e 1 PM para transformar sua pele em casca de árvore, recebendo +2 na Defesa até o fim da cena.'
#     personagem.caracteristicas['Empatia Selvagem'] = 'Você pode se comunicar com animais por meio de linguagem corporal e vocalizações. Você pode usar Adestramento para mudar atitude e persuasão com animais (veja Diplomacia, na página 118). Caso receba esta habilidade novamente, recebe +2 em Adestramento.'

def anao(personagem):
    '''
    
    '''
    personagem.caracteristicas.append(Habilidade('Visão no Escuro', 'Você vê no escuro'))
    personagem.caracteristicas.append(Habilidade('Conhecimento das Rochas', '+2 em testes de Percepção e Sobrevivência realizados no subterrâneo.'))
    personagem.deslocamento = 6
    personagem.caracteristicas.append(Habilidade('Devagar e Sempre', 'Seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'))
    personagem.PV.max += 3
    personagem.PV.extra_nivel['Duro como Pedra (anão)'] = 1
    personagem.caracteristicas.append(Habilidade('Tradição de Heredrimm', 'Você é perito nas armas tradicionais anãs. Para você, todos os machados, martelos, marretas e picaretas são armas simples. Você recebe +2 em ataques com essas armas.'))
    personagem.proficiencias += ['Machado', 'Martelo', 'Marreta', 'Picareta']

def dahllan(personagem):
    '''
    
    '''
    personagem.habilidades_poderes.append(Habilidade('Amiga das Plantas', 'Você pode lançar a magia Controlar Plantas (atributo-chave Sabedoria). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'))
    personagem.habilidades_poderes.append(Habilidade('Armadura de Allihanna', 'Você pode gastar uma ação de movimento e 1 PM para transformar sua pele em casca de árvore, recebendo +2 na Defesa até o fim da cena.'))
    personagem.caracteristicas.append(Habilidade('Empatia Selvagem', 'Você pode se comunicar com animais por meio de linguagem corporal e vocalizações. Você pode usar Adestramento para mudar atitude e persuasão com animais (veja Diplomacia, na página 118). Caso receba esta habilidade novamente, recebe +2 em Adestramento.'))


# def elfo(personagem):
#     '''
    
#     '''
#     # Graça de Glórienn
#     personagem.deslocamento = 12
#     # Sangue Mágico
#     personagem.PM.max += 1
#     personagem.PM.extra_nivel['Sangue Mágico'] = 1
#     # Sentidos Élficos
#     personagem.caracteristicas['Visão na Penumbra'] = 'Você vê na penumbra.'
#     personagem.pericias['Misticismo'].modificadores['Sentidos Élficos'] = 2
#     personagem.pericias['Percepção'].modificadores['Sentidos Élficos'] = 2


# def goblin(personagem):
#     '''
    
#     '''
#     # Engenhoso
#     personagem.caracteristicas['Engenhoso'] = 'Você não sofre penalidades em testes de perícia por não usar ferramentas. Se usar a ferramenta necessária, recebe +2 no teste de perícia.'
#     # Espelunqueiro
#     visao_escuro(personagem)
#     personagem.caracteristicas['Escalada'] = 'Deslocamento de escalada igual ao seu deslocamento terrestre.'
#     # Peste Esguia
#     personagem.tamanho = 'Pequeno'
#     personagem.deslocamento = 9
#     # Rato das Ruas
#     personagem.pericias['Fortitude'].modificadores['Rato das Ruas'] = 2
#     personagem.caracteristicas['Rato das Ruas'] = 'Sua recuperação de PV e PM nunca é inferior ao seu nível.'


def elfo(personagem):
    '''
    
    '''
    # Graça de Glórienn
    personagem.deslocamento = 12
    # Sangue Mágico
    personagem.PM.max += 1
    personagem.PM.extra_nivel.append(Habilidade('Sangue Mágico', '1'))
    # Sentidos Élficos
    personagem.caracteristicas.append(Habilidade('Visão na Penumbra', 'Você vê na penumbra.'))
    personagem.pericias['Misticismo'].modificadores['Sentidos Élficos'] = 2
    personagem.pericias['Percepção'].modificadores['Sentidos Élficos'] = 2


def goblin(personagem):
    '''
    
    '''
    # Engenhoso
    personagem.caracteristicas.append(Habilidade('Engenhoso', 'Você não sofre penalidades em testes de perícia por não usar ferramentas. Se usar a ferramenta necessária, recebe +2 no teste de perícia.'))
    # Espelunqueiro
    visao_escuro(personagem)
    personagem.caracteristicas.append(Habilidade('Escalada', 'Deslocamento de escalada igual ao seu deslocamento terrestre.'))
    # Peste Esguia
    personagem.tamanho = 'Pequeno'
    personagem.deslocamento = 9
    # Rato das Ruas
    personagem.pericias['Fortitude'].modificadores['Rato das Ruas'] = 2
    personagem.caracteristicas.append(Habilidade('Rato das Ruas', 'Sua recuperação de PV e PM nunca é inferior ao seu nível.'))



# def lefou(personagem):
#     '''
    
#     '''
#     # Cria da Tormenta
#     personagem.resistencias['Tormenta'] = 5
#     # Deformidade
#     for i in range(2): # mesma coias que no humano
#         if i == 0: print(f'A raça Humano lhe permite adquirir {2-i} perícias ou poderes. Quer uma perícia ou poder?')
#         else: print(f'A raça Humano lhe permite adquirir {2-i} perícia ou poder. Quer uma perícia ou poder?')
#         while True:
#             resp = formatacao(input())
#             if resp in 'pericia':
#                 # isso eh literalmente a função de escolher uma perícia
#                 pericia = escolhe_categoria(Palavra('perícia', 'perícias'), nomes_pericias, 1, personagem.pericias_treinadas())[0]
#                 personagem.adiciona_pericia(pericia)
#                 break
#             elif resp in 'poder':
#                 # programar escolha de poder_geral
#                 # poder_geral = escolhe_categoria()
#                 print('Escolher um poder ainda não foi implementado :(')
#                 break
#             else:
#                 print(f'{resp.title()} não é uma resposta válida. Tente novamente.')


# def minotauro(personagem):
#     # Chifres
#     personagem.habilidades_poderes['Chifres'] = 'Você possui uma arma natural de chifres (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com os chifres.'
#     # Couro Rígido
#     personagem.defesa.modificadores['Couro Rígido'] = 1
#     # Faro
#     personagem.caracteristicas['Faro'] = 'Você tem olfato apurado. Contra inimigos em alcance curto que não possa ver, você não fica desprevenido e camuflagem total lhe causa apenas 20% de chance de falha.'
#     # Medo de Altura
#     personagem.caracteristicas['Medo de Altura'] = 'Se estiver adjacente a uma queda de 3m ou mais de altura (como um buraco ou penhasco), você fica abalado.'


def lefou(personagem):
    '''
    
    '''
    # Cria da Tormenta
    personagem.resistencias['Tormenta'] = 5
    # Deformidade
    for i in range(2): # mesma coias que no humano
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


def minotauro(personagem):
    # Chifres
    personagem.habilidades_poderes.append(Habilidade('Chifres', 'Você possui uma arma natural de chifres (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com os chifres.'))
    # Couro Rígido
    personagem.defesa.modificadores['Couro Rígido'] = 1
    # Faro
    personagem.caracteristicas.append(Habilidade('Faro', 'Você tem olfato apurado. Contra inimigos em alcance curto que não possa ver, você não fica desprevenido e camuflagem total lhe causa apenas 20% de chance de falha.'))
    # Medo de Altura
    personagem.caracteristicas.append(Habilidade('Medo de Altura', 'Se estiver adjacente a uma queda de 3m ou mais de altura (como um buraco ou penhasco), você fica abalado.'))



# def qarren(personagem):
#     '''
    
#     '''
#     # Desejos
#     personagem.caracteristicas['Desejos'] = 'Se lançar uma magia que alguém tenha pedido desde seu último turno, o custo da magia diminui em -1 PM. Fazer um desejo ao qareen é uma ação livre.'
#     # Resistência Elemental
#     resistencia = escolhe_categoria(Palavra('resistência', 'resistências'), ['Frio', 'Eletricidade', 'Fogo', 'Ácido', 'Luz', 'Trevas'], escolhidos_antes=[])
#     personagem.resistencias[resistencia] = 10
#     # Tatuagem Mística
#     personagem.habilidades_poderes['Tatuagem Mística'] = 'Você pode lançar uma magia de 1o círculo a sua escolha (atributo-chave Carisma). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'


# def golem(personagem):
#     '''
    
#     '''
#     elementos = {'Água': 'Frio', 'Ar': 'Eletricidade', 'Fogo': 'Fogo', 'Terra': 'Ácido'}
#     # Chassi
#     personagem.deslocamento = 6
#     personagem.caracteristicas['Chassi'] = 'Seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'
#     personagem.defesa.modificadores['Chassi'] = 2
#     personagem.penalidade_armadura['Chassi (armadura natural golem)'] = -2
#     personagem.caracteristicas['Chassi 2'] = 'Você recebe +2 na Defesa, mas possui penalidade de armadura -2. Você leva um dia para vestir ou remover uma armadura (pois precisa acoplar as peças dela a seu chassi). Por ser acoplada, sua armadura não conta no limite de itens que você pode usar (mas você continua só podendo usar uma armadura).'
#     # Criatura Artificial
#     visao_escuro(personagem)
#     personagem.imunidades += ['Cansaço', 'Metabólico', 'Veneno']
#     personagem.caracteristicas['Criatura Artificial'] = 'não precisa respirar, alimentar-se ou dormir, mas não se beneficia de cura mundana e de itens da categoria alimentação. Você precisa ficar inerte por oito horas por dia para recarregar sua fonte de energia. Se fizer isso, recupera PV e PM por descanso em condições normais (golens não são afetados por condições boas ou ruins de descanso). Por fim, a perícia Cura não funciona em você, mas Ofício (artesão) pode ser usada no lugar dela.'
#     # Fonte Elemental
#     elemento = escolhe_categoria(Palavra('elemento', 'elementos'), elementos.keys(), escolhidos_antes=[], genero=1)[0]
#     personagem.caracteristicas['Fonte Elemental: ' + elemento.title()] = f'Você possui um espírito elemental de {elemento} preso em seu corpo. Você é imune a dano de {elementos[elemento]}. Se fosse sofrer dano mágico desse tipo, em vez disso cura PV em quantidade igual à metade do dano.'
#     # Propósito De Criação
#         # Incorporado em código já
    

def qarren(personagem):
    '''
    
    '''
    # Desejos
    personagem.caracteristicas.append(Habilidade('Desejos', 'Se lançar uma magia que alguém tenha pedido desde seu último turno, o custo da magia diminui em -1 PM. Fazer um desejo ao qareen é uma ação livre.'))
    # Resistência Elemental
    resistencia = escolhe_categoria(Palavra('resistência', 'resistências'), ['Frio', 'Eletricidade', 'Fogo', 'Ácido', 'Luz', 'Trevas'], escolhidos_antes=[])
    personagem.resistencias[resistencia] = 10
    # Tatuagem Mística
    personagem.habilidades_poderes.append(Habilidade('Tatuagem Mística', 'Você pode lançar uma magia de 1o círculo a sua escolha (atributo-chave Carisma). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'))


def golem(personagem):
    '''
    
    '''
    elementos = {'Água': 'Frio', 'Ar': 'Eletricidade', 'Fogo': 'Fogo', 'Terra': 'Ácido'}
    # Chassi
    personagem.deslocamento = 6
    personagem.caracteristicas.append(Habilidade('Chassi', 'Seu deslocamento não é reduzido por uso de armadura ou excesso de carga.'))
    personagem.defesa.modificadores['Chassi'] = 2
    personagem.penalidade_armadura['Chassi (armadura natural golem)'] = -2
    personagem.caracteristicas.append(Habilidade('Chassi', 'Você recebe +2 na Defesa, mas possui penalidade de armadura -2. Você leva um dia para vestir ou remover uma armadura (pois precisa acoplar as peças dela a seu chassi). Por ser acoplada, sua armadura não conta no limite de itens que você pode usar (mas você continua só podendo usar uma armadura).'))
    # Criatura Artificial
    visao_escuro(personagem)
    personagem.imunidades += ['Cansaço', 'Metabólico', 'Veneno']
    personagem.caracteristicas.append(Habilidade('Criatura Artificial', 'Você não precisa respirar, alimentar-se ou dormir, mas não se beneficia de cura mundana e de itens da categoria alimentação. Você precisa ficar inerte por oito horas por dia para recarregar sua fonte de energia. Se fizer isso, recupera PV e PM por descanso em condições normais (golens não são afetados por condições boas ou ruins de descanso). Por fim, a perícia Cura não funciona em você, mas Ofício (artesão) pode ser usada no lugar dela.'))
    # Fonte Elemental
    elemento = escolhe_categoria(Palavra('elemento', 'elementos'), elementos.keys(), escolhidos_antes=[], genero=1)[0]
    personagem.caracteristicas.append(Habilidade('Fonte Elemental: ' + elemento.title(), f'Você possui um espírito elemental de {elemento.lower()} preso em seu corpo. Você é imune a dano de {elementos[elemento].lower()}. Se fosse sofrer dano mágico desse tipo, em vez disso cura PV em quantidade igual à metade do dano.'))
    # Propósito De Criação
        # Incorporado em código já



# def hynne(personagem):
#     '''
    
#     '''
#     # Arremessador
#     personagem.caracteristicas['Arremessador'] = 'Quando faz um ataque à distância com uma funda ou uma arma de arremesso, seu dano aumenta em um passo.'
#     # Pequeno e Rechonchudo
#     personagem.tamanho = 'Pequeno'
#     personagem.deslocamento = 6
#     personagem.pericias['Enganação'].modficadores['Pequeno e Rechonchudo'] = 2
#     personagem.caracteristicas['Pequeno e Rechonchudo'] = 'Pode usar Destreza como atributo-chave de Atletismo (em vez de Força).'
#     # Sorte Salvadora
#     personagem.habilidades_poderes['Sorte Salvadora'] = 'Quando faz um teste de resistência, você pode gastar 1 PM para rolar este teste novamente.'


# def kliren(personagem):
#     '''
    
#     '''
#     # Híbrido
#     print('Parabéns, você ganhou uma perícia adicional por conta da raça Kliren')
#     pericia = escolhe_categoria(Palavra('perícia', 'perícias'), nomes_pericias, 1, personagem.pericias_treinadas())[0]
#     personagem.pericias[pericia].modificadores['Híbrido'] = 2
#     # Engenhosidade
#     personagem.habilidades_poderes['Engenhosidade'] = 'Quando faz um teste de perícia, você pode gastar 2 PM para somar sua Inteligência no teste. Você não pode usar esta habilidade em testes de ataque. Caso receba esta habilidade novamente, seu custo é reduzido em -1 PM.'
#     # Ossos Frágeis
#     personagem.fraquezas['Impacto'] = 1
#     personagem.caracteristicas['Ossos Frágeis'] = 'Você sofre 1 ponto de dano adicional por dado de dano de impacto. Exemplo: clava (1d6 -> 1d6+1 de dano), queda 3m (2d6 -> 2d6+2 de dano).'
#     # Vaguardista
#     personagem.proficiencias.append('armas de fogo')
#     personagem.pericias['Ofício'].modificadores['Vangaurdista'] = 2 # especificar oficio dps
    

def hynne(personagem):
    '''
    
    '''
    # Arremessador
    personagem.caracteristicas.append(Habilidade('Arremessador', 'Quando faz um ataque à distância com uma funda ou uma arma de arremesso, seu dano aumenta em um passo.'))
    # Pequeno e Rechonchudo
    personagem.tamanho = 'Pequeno'
    personagem.deslocamento = 6
    personagem.pericias['Enganação'].modificadores['Pequeno e Rechonchudo'] = 2
    personagem.caracteristicas.append(Habilidade('Pequeno e Rechonchudo', 'Pode usar Destreza como atributo-chave de Atletismo (em vez de Força).'))
    # Sorte Salvadora
    personagem.habilidades_poderes.append(Habilidade('Sorte Salvadora', 'Quando faz um teste de resistência, você pode gastar 1 PM para rolar este teste novamente.'))


def kliren(personagem):
    '''
    
    '''
    # Híbrido
    print('Parabéns, você ganhou uma perícia adicional por conta da raça Kliren')
    pericia = escolhe_categoria(Palavra('perícia', 'perícias'), nomes_pericias, 1, personagem.pericias_treinadas())[0]
    personagem.pericias[pericia].modificadores['Híbrido'] = 2
    # Engenhosidade
    personagem.habilidades_poderes.append(Habilidade('Engenhosidade', 'Quando faz um teste de perícia, você pode gastar 2 PM para somar sua Inteligência no teste. Você não pode usar esta habilidade em testes de ataque. Caso receba esta habilidade novamente, seu custo é reduzido em -1 PM.'))
    # Ossos Frágeis
    personagem.fraquezas['Impacto'] = 1
    personagem.caracteristicas.append(Habilidade('Ossos Frágeis', 'Você sofre 1 ponto de dano adicional por dado de dano de impacto. Exemplo: clava (1d6 -> 1d6+1 de dano), queda 3m (2d6 -> 2d6+2 de dano).'))
    # Vaguardista
    personagem.proficiencias.append('armas de fogo')
    personagem.pericias['Ofício'].modificadores['Vangaurdista'] = 2 # especificar oficio dps



# def medusa(personagem):
#     '''
    
#     '''
#     # Cria de Megalokk
#     visao_escuro(personagem)
#     # Natureza Venenosa
#     personagem.resistencias['Veneno'] = 5
#     personagem.habilidades_poderes['Natureza Venenosa'] = 'Pode gastar uma ação de movimento e 1 PM para envenenar uma arma que esteja usando. A arma causa perda de 1d12 pontos de vida. O veneno dura até você acertar um ataque ou até o fim da cena (o que acontecer primeiro).'
#     # Olhar Atordoante
#     personagem.habilidades_poderes['Olhar Atordoante'] = 'Você pode gastar uma ação de movimento e 1 PM para forçar uma criatura em alcance curto a fazer um teste de Fortitude (CD Car). Se a criatura falhar, fica atordoada por uma rodada (apenas uma vez por cena).'


# def osteon(personagem):
#     '''
    
#     '''
#     # Armadura Óssea
#     personagem.resistencias['Corte'] = 5
#     personagem.resistencias['Frio'] = 5
#     personagem.resistencias['Perfuração'] = 5
#     # Memória Póstuma
#         # PROGRAMAR FUTURAMENTE
#     # Natureza Esquelética
#     visao_escuro(personagem)
#     personagem.imunidades += ['Cansaço', 'Metabólico', 'Trevas', 'Veneno']
#     personagem.caracteristicas['Natureza Esquelética'] = 'Você não precisa respirar, alimentar-se ou dormir. Por fim, efeitos mágicos de cura de luz causam dano a você e você não se beneficia de itens da categoria alimentação, mas dano de trevas recupera seus PV.'
#     # Preço da Não Vida
#     personagem.caracteristicas['Preço da Não Vida'] = 'Você precisa passar oito horas sob a luz de estrelas ou no subterrâneo. Se fizer isso, recupera PV e PM por descanso em condições normais (osteon não são afetados por condições boas ou ruins de descanso). Caso contrário, sofre os efeitos de fome (p.319).'


def medusa(personagem):
    '''
    
    '''
    # Cria de Megalokk
    visao_escuro(personagem)
    # Natureza Venenosa
    personagem.resistencias['Veneno'] =  5
    personagem.habilidades_poderes.append(Habilidade('Natureza Venenosa', 'Pode gastar uma ação de movimento e 1 PM para envenenar uma arma que esteja usando. A arma causa perda de 1d12 pontos de vida. O veneno dura até você acertar um ataque ou até o fim da cena (o que acontecer primeiro).'))
    # Olhar Atordoante
    personagem.habilidades_poderes.append(Habilidade('Olhar Atordoante', 'Você pode gastar uma ação de movimento e 1 PM para forçar uma criatura em alcance curto a fazer um teste de Fortitude (CD Car). Se a criatura falhar, fica atordoada por uma rodada (apenas uma vez por cena).'))


def osteon(personagem):
    '''
    
    '''
    # Armadura Óssea
    personagem.resistencias['Corte'] = 5
    personagem.resistencias['Frio'] = 5
    personagem.resistencias['Perfuração'] = 5
    # Memória Póstuma
        # PROGRAMAR FUTURAMENTE
    # Natureza Esquelética
    visao_escuro(personagem)
    personagem.imunidades += ['Cansaço', 'Metabólico', 'Trevas', 'Veneno']
    personagem.caracteristicas.append(Habilidade('Natureza Esquelética', 'Você não precisa respirar, alimentar-se ou dormir. Por fim, efeitos mágicos de cura de luz causam dano a você e você não se beneficia de itens da categoria alimentação, mas dano de trevas recupera seus PV.'))
    # Preço da Não Vida
    personagem.caracteristicas.append(Habilidade('Preço da Não Vida', 'Você precisa passar oito horas sob a luz de estrelas ou no subterrâneo. Se fizer isso, recupera PV e PM por descanso em condições normais (osteon não são afetados por condições boas ou ruins de descanso). Caso contrário, sofre os efeitos de fome (p.319).'))



# def sereia_tritao(personagem):
#     '''
    
#     '''
#     # TROCAR / POR _
#     # Canção dos Mares
#     # PROGRAMAR COM MAGIA DEPOIS
#     personagem.habilidades_poderes['Canção dos Mares'] = 'Você pode lançar duas das magias a seguir: Amedrontar, Comando, Despedaçar, Enfeitiçar, Hipnotismo ou Sono (atributo-chave Carisma). Caso aprenda novamente uma dessas magias, seu custo diminui em -1 PM. @'

#     # Mestre do Tridente
#     personagem.proficiencias.append('Tridente')
#     personagem.caracteristicas['Mestre do Tridente'] = 'Para você, o tridente é uma arma simples. Além disso, você recebe +2 em rolagens de dano com azagaias, lanças e tridentes.'
#     # Tranformação Anfíbia
#     personagem.caracteristicas['Transformação Anfíbia'] = 'Você pode respirar debaixo d’água e possui uma cauda que fornece deslocamento de natação 12m. Quando fora d’água, sua cauda desaparece e dá lugar a pernas (deslocamento 9m). Se permanecer mais de um dia sem contato com água, você não recupera PM com descanso até voltar para a água (ou, pelo menos, tomar um bom banho!).'


# def silfide(personagem):
#     '''
    
#     '''
#     # Asas de Borboleta
#     personagem.tamanho = 'Minúsculo'
#     personagem.imunidades.append('Queda')
#     personagem.habilidades_poderes['Asas de Borboleta'] = 'Você pode gastar 1 PM por rodada para voar com deslocamento de 12m.'
#     personagem.caracteristicas['Asas de Borboleta'] = 'Você pode pairar a 1,5m do chão com deslocamento 9m. Isso permite que você ignore terreno difícil e o torna imune a dano por queda (a menos que esteja inconsciente).'
#     # Espírito da Natureza
#     personagem.caracteristicas['Visão na Penumbra'] = 'Você vê na penumbra.'
#     personagem.caracteristicas['Espírito da Natureza'] = 'Você é uma criatura do tipo espírito e pode falar com animais livremente.'
#     # Magia das Fadas
#     personagem.habilidades_poderes['Magia das Fadas'] = 'Você pode lançar duas das magias a seguir (atributo-chave Carisma): Criar Ilusão, Enfeitiçar, Luz (como uma magia arcana) e Sono. Caso aprenda novamente uma dessas magias, seu custo diminui em -1 PM. @'


def sereia_tritao(personagem):
    '''
    
    '''
    # TROCAR / POR _
    # Canção dos Mares
    # PROGRAMAR COM MAGIA DEPOIS
    personagem.habilidades_poderes.append(Habilidade('Canção dos Mares', 'Você pode lançar duas das magias a seguir: Amedrontar, Comando, Despedaçar, Enfeitiçar, Hipnotismo ou Sono (atributo-chave Carisma). Caso aprenda novamente uma dessas magias, seu custo diminui em -1 PM. @'))

    # Mestre do Tridente
    personagem.proficiencias.append('Tridente')
    personagem.caracteristicas.append(Habilidade('Mestre do Tridente', 'Para você, o tridente é uma arma simples. Além disso, você recebe +2 em rolagens de dano com azagaias, lanças e tridentes.'))
    # Tranformação Anfíbia
    personagem.caracteristicas.append(Habilidade('Transformação Anfíbia', 'Você pode respirar debaixo d’água e possui uma cauda que fornece deslocamento de natação 12m. Quando fora d’água, sua cauda desaparece e dá lugar a pernas (deslocamento 9m). Se permanecer mais de um dia sem contato com água, você não recupera PM com descanso até voltar para a água (ou, pelo menos, tomar um bom banho!).'))


def silfide(personagem):
    '''
    
    '''
    # Asas de Borboleta
    personagem.tamanho = 'Minúsculo'
    personagem.imunidades.append('Queda')
    personagem.habilidades_poderes.append(Habilidade('Asas de Borboleta', 'Você pode gastar 1 PM por rodada para voar com deslocamento de 12m.'))
    personagem.caracteristicas.append(Habilidade('Asas de Borboleta', 'Você pode pairar a 1,5m do chão com deslocamento 9m. Isso permite que você ignore terreno difícil e o torna imune a dano por queda (a menos que esteja inconsciente).'))
    # Espírito da Natureza
    personagem.caracteristicas.append(Habilidade('Visão na Penumbra', 'Você vê na penumbra.'))
    personagem.caracteristicas.append(Habilidade('Espírito da Natureza', 'Você é uma criatura do tipo espírito e pode falar com animais livremente.'))
    # Magia das Fadas
    personagem.habilidades_poderes.append(Habilidade('Magia das Fadas', 'Você pode lançar duas das magias a seguir (atributo-chave Carisma): Criar Ilusão, Enfeitiçar, Luz (como uma magia arcana) e Sono. Caso aprenda novamente uma dessas magias, seu custo diminui em -1 PM. @'))



# def suraggel_aggelus(personagem):
#     '''
    
#     '''
#     # Herança Divina
#     personagem.caracteristicas['Herança Divina'] = 'Você é uma criatura do tipo espírito.'
#     visao_escuro(personagem)
#     # Luz Sagrada (Aggelus)
#     personagem.habilidades_poderes['Luz Sagrada'] = 'Pode lançar Luz (como uma magia divina; atributo-chave Carisma). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'
#     personagem.pericias['Diplomacia'].modifcadores['Luz Sagrada'] = 2
#     personagem.pericias['Intuição'].modifcadores['Luz Sagrada'] = 2




# def suraggel_sulfure(personagem):
#     '''
    
#     '''
#     # Herança Divina
#     personagem.caracteristicas['Herança Divina'] = 'Você é uma criatura do tipo espírito.'
#     visao_escuro(personagem)
#     # Sombras Profanas
#     personagem.habilidades_poderes['Sombras Profanas'] = 'Pode lançar Escuridão (como uma magia divina; atributo-chave Inteligência). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'
#     personagem.pericias['Enganação'].modificadores['Sombras Profanas'] = 2
#     personagem.pericias['Furtividade'].modificadores['Sombras Profanas'] = 2


def suraggel_aggelus(personagem):
    '''
    
    '''
    # Herança Divina
    personagem.caracteristicas.append(Habilidade('Herança Divina', 'Você é uma criatura do tipo espírito.'))
    visao_escuro(personagem)
    # Luz Sagrada (Aggelus)
    personagem.habilidades_poderes.append(Habilidade('Luz Sagrada', 'Pode lançar Luz (como uma magia divina; atributo-chave Carisma). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'))
    personagem.pericias['Diplomacia'].modificadores['Luz Sagrada'] = 2
    personagem.pericias['Intuição'].modificadores['Luz Sagrada'] = 2


def suraggel_sulfure(personagem):
    '''
    
    '''
    # Herança Divina
    personagem.caracteristicas.append(Habilidade('Herança Divina', 'Você é uma criatura do tipo espírito.'))
    visao_escuro(personagem)
    # Sombras Profanas
    personagem.habilidades_poderes.append(Habilidade('Sombras Profanas', 'Pode lançar Escuridão (como uma magia divina; atributo-chave Inteligência). Caso aprenda novamente essa magia, seu custo diminui em -1 PM. @'))
    personagem.pericias['Enganação'].modificadores['Sombras Profanas'] = 2
    personagem.pericias['Furtividade'].modificadores['Sombras Profanas'] = 2



# def trog(personagem):
#     '''
    
#     '''
#     # Mau Cheiro
#     personagem.habilidades_poderes['Mau Cheiro'] = 'Você pode gastar uma ação padrão e 2 PM para expelir um gás fétido. Todas as criaturas (exceto trogs) em alcance curto devem passar em um teste de Fortitude contra veneno (CD Con) ou ficarão enjoadas durante 1d6 rodadas. Uma criatura que passe no teste de resistência fica imune a esta habilidade por um dia.'
#     # Mordida
#     personagem.habilidades_poderes['Mordida'] = 'Você possui uma arma natural de mordida (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida.'
#     # Reptiliano
#     personagem.caracteristicas['Reptiliano'] = 'Você é uma criatura do tipo monstro.'
#     visao_escuro(personagem)
#     personagem.defesa.modificadores['Reptiliano'] = 1
#     personagem.caracteristicas['Reptiliano 2'] = 'Se você estiver sem armadura ou roupas pesadas, +5 em Furtividade.'
#     # Sangue Frio
#     personagem.fraquezas['Frio'] = 1
#     personagem.caracteristicas['Sangue Frio'] = 'Você sofre 1 ponto de dano adicional por dado de dano de frio.'


def trog(personagem):
    '''
    
    '''
    # Mau Cheiro
    personagem.habilidades_poderes.append(Habilidade('Mau Cheiro', 'Você pode gastar uma ação padrão e 2 PM para expelir um gás fétido. Todas as criaturas (exceto trogs) em alcance curto devem passar em um teste de Fortitude contra veneno (CD Con) ou ficarão enjoadas durante 1d6 rodadas. Uma criatura que passe no teste de resistência fica imune a esta habilidade por um dia.'))
    # Mordida
    personagem.habilidades_poderes.append(Habilidade('Mordida', 'Você possui uma arma natural de mordida (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida.'))
    # Reptiliano
    personagem.caracteristicas.append(Habilidade('Reptiliano', 'Você é uma criatura do tipo monstro.'))
    visao_escuro(personagem)
    personagem.defesa.modificadores['Reptiliano'] = 1
    personagem.caracteristicas.append(Habilidade('Reptiliano 2', 'Se você estiver sem armadura ou roupas pesadas, +5 em Furtividade.'))
    # Sangue Frio
    personagem.fraquezas['Frio'] = 1
    personagem.caracteristicas.append(Habilidade('Sangue Frio', 'Você sofre 1 ponto de dano adicional por dado de dano de frio.'))




funcoes_racas = {
    'humano': humano,
    'anao': anao,
    'dahllan': dahllan,
    'elfo': elfo,
    'goblin': goblin,
    'lefou': lefou,
    'minotauro': minotauro,
    'qarren': qarren,
    'golem': golem,
    'hynne': hynne,
    'kliren': kliren,
    'medusa': medusa,
    'osteon': osteon,
    'sereia/tritao': sereia_tritao,
    'silfide': silfide,
    'suraggel (aggelus)': suraggel_aggelus,
    'suraggel (sulfure)': suraggel_sulfure,
    'trog': trog


}