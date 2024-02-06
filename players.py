from dataclasses import dataclass, field
from typing import DefaultDict
from random import randint
import os
import ast
import re
import unicodedata
import sys
# from funcoes_especificas import racas
# from funcoes_especificas import classes
# from funcoes_especificas import origens


# paths
path = '/home/maraolt/Documents/projects/automatic_rpg_battles' # ubuntu desktop/notebook


'''
URGENTE:
-[] Mover todas as funções para fora de Personagem() para poder criar um arquivo com apenas as classes
-[] Criar método __init__ para criar pacote python

Criação de Personagem:
01-[X] Definindo os 6 atributos: Forca, Destreza, Constituicao, Inteligencia, Sabedoria e Carisma
    -[] Refazer sistema de pontos para conseguir colocar: 'forca 4'/ 'for -1' e coisas do tipo em apenas 1 linha
    -[X] Sistema para escolher os atributos aleatoriamente
02-[X] Escolhendo raça: 17 raças que alteram atributos e adicionam habilidades
    -[X] Adquirir as infos de racas.txt para serem usadas
    -[X] Criar função que adiciona os modificadores de atributos da raça
    -[] Criar uma função para cada habilidade (futuramente...)
    -[] Criar excessão do golem não poder escolher origem e sim um poder geral
03-[X] Escolhendo classe: 14 classes
    -[X] Adquirir as infos de classes.txt para serem usadas
    -[X] Criar função que adiciona os PMs e PVs
    -[X] Adicionar perícias (futuramente...)
04-[X] Escolhendo origem: 35 origens
    -[X] Adquirir as infos de origens.txt para serem usadas
    -[X] Você escolhe dois benefícios da lista de benefícios -> fazer depois de implementar perícias
05-[X] Escolhendo divindade (opcional): 20 divindades
    -[X] Adquirir as infos de divindades.txt para serem usadas 
    -[X] Apenas certas classes ou raças podem ser devotos de certas divindades
06-[X] Escolhendo Pericias: 30 perícias
    -[] Criar forma personalizada para a perícia Ofício
    -[X] Função que calcula o bônus de perícia
-[] Percebi que preciso todas as funções de raças e classes para continuar daqui em diante
07-[] Anotando Equipamento Inicial: definido pela classe e origem
08-[] Toques finais: PV, PM, ataques, nome, deslocamento, defesa, tamanho...
09-[] Salvar personagem criado em arquivo nome_personagem.txt
10-[] Importar personagem em arquivos nome_personagem.txt para um objeto dentro do programa
11-[] Escolhendo magias: apenas 4 classes possuem magias (arcanista, bardo, clerigo e druida) - (necessária ajuda ou maior conhecimento de web scraping)
12-[] Combates entre personagens
13-[] Criar loja de compras com saldo do personagem
14-[] Funções de:
    -[] Habilidades
    -[] Poderes
    -[] Magias
15-[] Fichas de Ameaças (necessário maior conhecimento de web scraping para fazer todos os inimigos)


Anotações gerais:
-[] fazer comentarios nas funções
-[] verificar se tem lugares no código que necessitam de um 'break'
-[] implementar em todo o código a função de ignorar acentos
'''

nomes_atributos = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']
nomes_pericias = {'Acrobacia', 'Adestramento', 'Atletismo', 'Atuação', 'Cavalgar', 'Conhecimento',
                       'Conhecimento', 'Cura', 'Diplomacia', 'Enganação', 'Fortitude', 'Furtividade',
                       'Guerra', 'Iniciativa', 'Intimidação', 'Intuição', 'Investigação', 'Jogatina',
                       'Ladinagem', 'Luta', 'Misticismo', 'Nobreza', 'Ofício', 'Percepção',
                       'Pilotagem', 'Pontaria', 'Reflexos', 'Religião', 'Sobrevivência', 'Vontade'}


@dataclass
class Palavra:
    singular: str = ''
    plural: str = ''


@dataclass 
class Atributo:
    valor_pontos: int
    valor_rolamentos: int
    modificador: int
    descricao: str
    pericias: str


    def calcula_modificador_pontos(self, pontos_gastos):
        '''
        Esta função faz o uso da Tabela 1-1: Atributos (p.17) para fazer a conversão
        do sistema de pontos para os modificadores dos atributos básicos. A função
        recebe os pontos_gastos em 1 atributo e retorna o valor do modificador. 
        '''
        if pontos_gastos in [-1, 0, 1, 2, 3]:
            return min(pontos_gastos, 2)
        elif pontos_gastos in [4, 5, 6]:
            return 3
        elif pontos_gastos in [7]:
            return 4
            

    def calcula_modificador_rolagens(self, todas_rolagens):
        '''
        Esta função faz o uso da Tabela 1-1: Atributos (p.17) para fazer a conversão
        do sistema de rolagens para os modificadores dos atributos básicos. A função
        recebe os todas_rolagens e retorna os valores de todos os modificadores das
        rolagens. 
        '''
        tam = len(todas_rolagens)
        lista_modificadores = []
        for i in range(tam):
            lista_modificadores.append(max(((todas_rolagens[i]//2)-5), -2))
        
        return lista_modificadores


penalidade_treino = ['adestramento', 'atuação', 'conhecimento', 'guerra', 'jogatina', 'ladinagem',
                      'misticismo', 'nobreza', 'ofício', 'pilotagem', 'religião']
penalidade_armadura = ['acrobacia', 'furtividade', 'ladinagem']


@dataclass
class Pericia:
    atributo: str = ''
    treinada: bool = False
    modificadores: DefaultDict[str, int] = field(default_factory=dict)
    modificador: int = 0
    

dicionario_pericias = {'Acrobacia': Pericia('Destreza'), 'Adestramento': Pericia('Carisma'), 
                       'Atletismo': Pericia('Força'), 'Atuação': Pericia('Carisma'),
                       'Cavalgar': Pericia('Destreza'), 'Conhecimento': Pericia('Inteligência'),
                       'Conhecimento': Pericia('Inteligência'), 'Cura': Pericia('Sabedoria'),
                       'Diplomacia': Pericia('Carisma'), 'Enganação': Pericia('Carisma'),
                       'Fortitude': Pericia('Constituição'), 'Furtividade': Pericia('Destreza'),
                       'Guerra': Pericia('Inteligência'), 'Iniciativa': Pericia('Destreza'),
                       'Intimidação': Pericia('Carisma'), 'Intuição': Pericia('Sabedoria'),
                       'Investigação': Pericia('Inteligência'), 'Jogatina': Pericia('Carisma'),
                       'Ladinagem': Pericia('Destreza'), 'Luta': Pericia('Força'),
                       'Misticismo': Pericia('Inteligência'), 'Nobreza': Pericia('Inteligência'),
                       'Ofício': Pericia('Inteligência'), 'Percepção': Pericia('Sabedoria'),
                       'Pilotagem': Pericia('Destreza'), 'Pontaria': Pericia('Destreza'),
                       'Reflexos': Pericia('Destreza'), 'Religião': Pericia('Sabedoria'),
                       'Sobrevivência': Pericia('Sabedoria'), 'Vontade': Pericia('Sabedoria')}


# aqui eu vou escrever todas as habilidades em codigo
@dataclass
class Habilidade:
    nome: str = ''
    descricao: str = ''


    def imprime(self):
        print(f'-{self.nome.upper()}')
        if self.descricao is not None:
            print(self.descricao + '\n')


@dataclass
class Pontos:
    '''
    Objeto usado para os PVs e PMs. Armazena atual, maximo e temporário.
    '''
    atual: int = 0
    max: int = 0
    temp: int = 0


@dataclass
class Raca:
    '''
    Objeto usado para todas as 17 raças existentes.
    '''
    nome: str = ''
    modificadores_atributos: str = ''
    habilidades: list = None


    def imprime(self):
        '''
        Esta função simplesmente imprime as características que a classe adiciona
        '''
        print('-'*40)
        print(self.nome.upper())
        print(f'Atributos: {self.modificadores_atributos}\n')
        for habilidade in self.habilidades:
            habilidade.imprime()
        print('-'*40)


@dataclass
class Classe:
    '''
    Objeto usado para todas as 14 classes existentes.
    '''
    nome: str = ''
    descricao: str = ''
    atributo: list = None
    PV: int = 0
    PM: int = 0
    pericias: list = None
    proficiencias: list = None
    habilidades: list = None


    def escolhe_pericias(self, conj_pericias_txt):
        '''
        Esta função recebe as perícias em forma de texto e através de perguntas ao usuário
        seleciona quais perícias a classe adicionará ao personagem.
        '''

        pericias_finais = []
        escolha = re.compile(r'^escolha (\d+) entre: ')
        for pericias_txt in conj_pericias_txt:
            if ' ou ' in pericias_txt.lower():
                pericias_txt = pericias_txt.split(' ou ')
                while True:
                    resp = input(f'Em qual pericia você quer ser treinado: {pericias_txt[0].title()} ou {pericias_txt[1].title()}? ').lower()
                    encontrou = False
                    for pericia in pericias_txt:
                        if resp in pericia:
                            pericias_finais.append(pericia)
                            print(f'Perícia em {pericia.title()} ')
                            encontrou = True
                            break
                            
                    if not encontrou:
                        print(f'{resp.title()} não é uma das opções. ', end='')
                    else:
                        break
            elif escolha.match(pericias_txt):
                n_escolhas = int(escolha.match(pericias_txt).group(1))
                pericias_txt = pericias_txt[pericias_txt.index(':')+2:].strip('\n').strip().split(', ')
                
                pericias_finais = pericias_finais + escolhe_categoria(Palavra('perícia', 'perícias'), pericias_txt, n_escolhas, pericias_finais, genero = 0)
            else:
                pericias_finais.append(pericias_txt)
                print(f'Perícia em {pericias_txt.title()}.')

        self.pericias = pericias_finais


    def imprime(self):
        '''
        Esta função simplesmente imprime as informações que a classe adiciona ao personagem.
        '''
        print('-'*40)
        print(self.nome.upper())
        print(self.descricao)
        if len(self.atributo) > 1:
            print(f'\nOs atributos mais importantes para essa classe são: {self.atributo}')
        else:
            print(f'\nO atributo mais importante para essa classe é: {self.atributo}')
        print(f'PV: {self.PV} + Constituição ({self.PV//4} por nível)')
        print(f'PM: {self.PM} ({self.PM} por nível)')
        print(f'Perícias: {self.pericias}')
        print(f'Proficiências: {self.proficiencias}')
        print(f'Habilidades de Classe: ')
        i = 1
        for habilidade in self.habilidades:
            print(f'{i}- {habilidade}')
            i += 1
        print('-'*40)


@dataclass
class Origem:
    '''
    
    '''
    nome: str = ''
    beneficios: list = None
    itens: list = None


    def imprime(self):
        '''
        Esta função simplesmente imprime as características que a origem adiciona
        '''
        print('-'*40)
        print(self.nome.upper())
        print(f'Benefícios: {self.beneficios}')
        print(f'Itens: {self.itens}')
        print('-'*40)


@dataclass
class Divindade:
    nome: str = ''
    crencas_objetivos: str = ''
    simbolo: str = ''
    energia: str = ''
    arma: str = ''
    devotos: list = None
    poderes: list = None
    obrigacoes_restricoes: str = ''


    def verifica_devotos(self, raca, classe, devotos):
        '''
        Verifica se a raça ou classe do personagem pertence a devotos da divindade retornando True ou False
        '''
        for devoto in devotos:
            if formatacao(raca) in formatacao(devoto) or formatacao(classe) in formatacao(devoto):
                return True
        
        print(f'Infelizmente você não pode ser devoto dessa divindade, pois apenas {devotos} podem ser devotos.')
        return False


    def imprime(self):
        '''
        Esta função simplesmente imprime as características que a divindade adiciona
        '''
        print('-'*40)
        print(self.nome.upper())
        print(f'Crenças e Objetivos: {self.crencas_objetivos}')
        print(f'Símbolo Sagrado: {self.simbolo}')
        print(f'Energia: {self.energia}')
        print(f'Arma Preferida: {self.arma}')
        print(f'Devotos: {self.devotos}')
        print(f'Poderes Concedidos: {self.poderes}')
        print(f'Obrigações & Restrições: {self.obrigacoes_restricoes}')
        print('-'*40)


dicionario_atributos = {'Força': Atributo(0, 10, 0, '''Força (FOR): Seu poder muscular. A Força é aplicada em testes de Atletismo e Luta;
                                 rolagens de dano corpo a corpo ou com armas de arremesso, e testes de Força
                                 para levantar peso e atos similares.''',\
                                      'Atletismo, Luta'), \
                'Destreza': Atributo(0, 10, 0, 'Destreza (DES): Sua agilidade, reflexos, equilíbrio e coordenação motora. A Destreza é\
                                 aplicada na Defesa e em testes de Acrobacia, Cavalgar, Furtividade, Iniciativa,\
                                 Ladinagem, Pilotagem, Pontaria e Reflexos.',\
                                      'Acrobacia, Cavalgar, Furtividade, Iniciativa, Ladinagem, Pilotagem, Pontaria, Reflexos'), \
                'Constituição': Atributo(0, 10, 0, 'Constituição (CON): Sua saúde e vigor. A Constituição é aplicada aos pontos de vida\
                                 iniciais e por nível e em testes de Fortitude. Se a Constituição muda, seus pontos de vida\
                                 aumentam ou diminuem retroativamente de acordo.',\
                                      'Fortitude'), \
                'Inteligência': Atributo(0, 10, 0, 'Inteligência (INT): Sua capacidade de raciocínio, memória e educação.\
                                 A Inteligência é aplicada em testes de Conhecimento, Guerra, Investigação,\
                                 Misticismo, Nobreza e Ofício. Além disso, se sua Inteligência for positiva,\
                                 você recebe um número de perícias treinadas igual ao valor dela (não precisam ser\
                                 da sua classe).',\
                                      'Conhecimento, Guerra, Investigação, Misticismo, Nobreza, Ofício'), \
                'Sabedoria': Atributo(0, 10, 0, 'Sabedoria (SAB): Sua observação, ponderação e determinação. A Sabedoria é aplicada\
                                 em testes de Cura, Intuição, Percepção, Religião, Sobrevivência e Vontade.',\
                                      'Cura, Intuição, Percepção, Religião, Sobrevivência, Vontade'), \
                'Carisma': Atributo(0, 10, 0, 'Carisma (CAR): Sua força de personalidade e capacidade de persuasão, além de uma mistura de simpatia\
                                 e beleza. O Carisma é aplicado em testes de Adestramento, Atuação, Diplomacia,\
                                 Enganação, Intimidação e Jogatina.',\
                                      'Adestramento, Atuação, Diplomacia, Enganação, Intimidação, Jogatina')}


raca_default = Raca('', '', '')
classe_default = Classe('', '', [], 0, 0, [], [], [])
pontos_default1 = Pontos(0, 0, 0)
pontos_default2 = Pontos(0, 0, 0)
origem_default = Origem('', [], [])
divindade_default = Divindade('', '', '', '', '', [], [])


@dataclass
class Personagem:
    '''
    Este é o objeto que representa um personagem. É o objeto principal para fichas de personagens e grande
    parte do código é relacionado a esse objeto e seus atributos.
    '''
    nome: str = ''
    jogador: str = ''
    nivel: int = 1
    raca: Raca = field(default_factory=Raca)
    classe: Classe = field(default_factory=Classe)
    origem: Origem = field(default_factory=Origem)
    divindade: Divindade = field(default_factory=Divindade)
    atributos: DefaultDict[str, Atributo] = field(default_factory=dict)
    pericias: DefaultDict[str, Pericia] = field(default_factory=dict)
    habilidades_poderes: DefaultDict[str, str] = field(default_factory=dict)
    equipamento: list = None
    PV: Pontos = field(default_factory=Pontos)
    PM: Pontos = field(default_factory=Pontos)
    # defesa: Defesa() = defesa_default
    # tamanho: Tamanho() = tamanho_default


    def imprime(self):
        '''
        Imprime as informações básicas do personagem criado
        '''
        print(f'{self.nome} ({self.jogador})')
        print(f'{self.raca.nome.title()}/{self.classe.nome.title()} {self.nivel}')
        print(f'PV: {self.PV.atual}/{self.PV.max}')
        print(f'PM: {self.PM.atual}/{self.PM.max}')
        # print(f'Defesa: {self.defesa if self.defesa > 0 else "Ainda não finalizado"}')
        self.imprime_atributos()
        self.raca.imprime()
        self.classe.imprime()


    def imprime_pericias(self):
        print('PERÍCIAS: ')
        for pericia in nomes_pericias:
            print(f'{pericia} ({self.pericias[pericia].atributo[:3]}): {self.pericias[pericia].modificador} {"(T)" if self.pericias[pericia].treinada else ""}')


    def pericias_treinadas(self):
        pericias_treinadas = []
        for pericia in nomes_pericias:
            if self.pericias[pericia].treinada:
                pericias_treinadas.append(pericia)
        
        return pericias_treinadas


    def bonus_treinamento(self):
        '''
        Retorna o bônus de treinamento de perícias de acordo com o nível do jogador
        '''
        if self.nivel < 7: return 2
        elif self.nivel >= 7 and self.nivel < 15: return 4
        else: return 6


    def modificadores(self, pericia):
        '''
        Faz a soma de todos os modificadores que estão atuando em uma certa perícias passada como argumento
        e retona a soma dos modificadores.
        '''
        soma = 0
        for modificador in self.pericias[pericia].modificadores:
            soma += modificador

        return soma


    def calcula_pericia(self, pericia):
        '''
        Esta função faz o cálculo do modificador de uma perícia analisando todos os aspectos que podem afeta-lá
        atualizando o modificador dessa perícia que é passada como argumento.
        '''

        # bônus de perícia = modificador atributo + metade do nível + bônus treinamento (se for treinada)
        self.pericias[pericia].modificador = self.atributos[self.pericias[pericia].atributo].modificador + self.nivel//2 +\
        (self.bonus_treinamento() if self.pericias[pericia].treinada else 0) + self.modificadores(pericia)


    def imprime_atributos(self):
        '''
        Esta função simplesmente imprime no terminal todos os atributos do personagem e seus respectivos modificadores.
        '''
        print('\nAtributos:')
        for nome_atributo in nomes_atributos:
            print(f'-{nome_atributo}: {self.atributos[nome_atributo].modificador}')
        print()


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



def define_atributos_pontos(personagem):
    '''
    Esta função realiza automaticamente o cálculo dos valores
    dos modificadores dos atributos básicos de acordo com os pedidos
    do usuário utilizando a regra dos pontos (p.17).
    '''

    pontos = 10
    print('''Pontos. Você começa com todos os atributos
em 0 e recebe 10 pontos para aumentá-los. O custo
para aumentar cada atributo está descrito na tabela
abaixo. Você também pode reduzir um atributo para
-1 para receber 1 ponto adicional.''')
    while True:
        personagem.imprime_atributos()
        print('Para sair desta função escreva: "sair".')
        atr = input('Escolha um atributo (for, des, con, int, sab, car): ').lower()
        if atr == 'sair':
            if pontos != 0:
                print('Você ainda não pode sair, pois deve gastar todos os pontos (positivos e/ou negativos).')
            else:
                break
        for nome_atributo in nomes_atributos:
            if atr in formatacao(nome_atributo):
                while True:
                    try:
                        pontos_usados = int(input(f'Você possui {pontos} pontos. Quantos pontos deseja gastar em {nome_atributo}? '))
                        if pontos_usados > 7 or pontos_usados < -1:
                            print('O número de pontos usado em um atributo deve ser no máximo 7 e no mínimo -1. Tente novamente.')
                            continue
                        personagem.atributos[nome_atributo].valor_pontos = pontos_usados
                        modificador = personagem.atributos['Força'].calcula_modificador_pontos(pontos_usados)
                        personagem.atributos[nome_atributo].modificador = modificador
                        pontos_gastos = sum(atributo.valor_pontos for atributo in personagem.atributos.values())
                        pontos = 10 - pontos_gastos
                        print(f'Seu modificador de {nome_atributo} é {modificador} e você possui mais {pontos} pontos.')
                        break
                    except ValueError:
                        erro()


def rolagens_atributos():
    '''
    Esta função faz a rolagem de dados para os atributos, retornando 'todas_rolagens'
    '''
    todas_rolagens = []
    for _ in range(6):
        rolagens_somadas = []
        for _ in range(4):
            rolagens_somadas.append(rolagem('1d6'))
        rolagens_somadas = sorted(rolagens_somadas)
        todas_rolagens.append(sum(rolagens_somadas[1:]))
    todas_rolagens = sorted(todas_rolagens, reverse=True)

    return todas_rolagens


def define_atributos_rolagens(personagem):
    '''
    Esta função realiza automaticamente o cálculo dos valores
    dos modificadores dos atributos básicos de acordo com os pedidos
    do usuário utilizando a regra das rolagens (p.17).
    '''

    print('Rolagens. Role 4d6, descarte o menor e some os outros três.\
Anote o resultado. Repita esse processo cinco vezes, até obter um total de seis números.\
Então, converta esses números em atributos conforme a tabela abaixo.\
Por exemplo, se você rolar 13, 8, 15, 18, 10 e 9, seus atributos serão 1, -1, 2, 4, 0 e -1.\
Distribua esses valores entre os seis atributos como quiser.\
Caso seus atributos não somem pelo menos 6, role novamente o menor valor.\
Repita esse processo até seus atributos somarem 6 ou mais.\n\
Observação: esse programa fará tudo automaticamente e apena lhe fornecerá os resultados dos dados!')
    
    todas_rolagens = rolagens_atributos()
    lista_modificadores = personagem.atributos['Força'].calcula_modificador_rolagens(todas_rolagens)

    print(f'Todas as rolagens foram realizadas e aqui estão todos os resultados [modificado (rolagem)]: ')
    for i in range(len(lista_modificadores)):
        print(f'{lista_modificadores[i]} ({todas_rolagens[i]}) | ', end='')
    print()

    i = 0
    escolhidos = []
    while i < (len(lista_modificadores)):
        atr = input(f'Selecione em qual atributo você quer colocar o valor {lista_modificadores[i]} (for, des, con, int, sab, car): ').lower()
        try:
            for nome_atributo in nomes_atributos:
                if atr in formatacao(nome_atributo):
                    if nome_atributo not in escolhidos:
                        escolhidos.append(nome_atributo)
                        personagem.atributos[nome_atributo].valor_rolamentos = todas_rolagens[i]
                        personagem.atributos[nome_atributo].modificador = lista_modificadores[i]
                        for escolhido in escolhidos:
                            print(f'{escolhido}: {personagem.atributos[escolhido].modificador}')

                        i += 1
                    else:
                        print(f'Você já escolheu o atributo {nome_atributo}, por favor escolha outro ainda não escolhido.')
        except ValueError:
            erro()
    
    print('Todos os atributos foram escolhidos.')


def define_atributos_manualmente(personagem):
    '''
    Esta funcao deixa o usuario definir os atributos manualmente
    '''

    print('Aqui voce colocara os atributos manualmente.')

    i = 0
    while i < len(nomes_atributos):
        try:
            atr = int(input(f'Qual o modificador de {nomes_atributos[i]}?\n'))
            personagem.atributos[nomes_atributos[i]].modificador = atr
            i += 1
            for j in range(i):
                print(f'-{nomes_atributos[j]}: {personagem.atributos[nomes_atributos[j]].modificador}')

        except ValueError:
            erro()


def define_atributos_aleatoriamente(personagem):
    '''
    Esta função utiliza do sistema por rolagens para definir aleatoriamente os atributos do personagem
    '''
    todas_rolagens = rolagens_atributos()
    lista_modificadores = personagem.atributos['Força'].calcula_modificador_rolagens(todas_rolagens)
    escolhido = []
    n_modificador = 0
    while n_modificador < len(nomes_atributos):
        aleatorio = randint(0, 5)
        if nomes_atributos[aleatorio] not in escolhido:
            personagem.atributos[nomes_atributos[aleatorio]].modificador = lista_modificadores[n_modificador]
            n_modificador += 1
    print('Pronto! Seus atributos foram aleatoriamente gerados e distribuidos.')


def define_atributos(personagem):
    '''
    Esta função simplesmente pergunta ao usuário qual das duas maneiras de definir os atributos básicos 
    ele prefere usar (pontos ou rolagens) e direciona-o para a respectiva função dependendo de sua resposta.
    '''
    while True:
        resp = input('Há quatro maneiras de definir seus atributos: com pontos, rolagens, manualmente ou aleatório. Escolha a que preferir: (Pontos OU Rolagens OU Manualmente OU Aleatorio)\n').lower()
        if resp in 'pontos' or 'pontos' in resp:
            define_atributos_pontos(personagem)
            break
        elif resp in 'rolagens' or resp in 'rolagem' or 'rolagens' in resp or 'rolagem' in resp:
            define_atributos_rolagens(personagem)
            break
        elif resp in 'manualmente':
            define_atributos_manualmente(personagem)
            break
        elif resp in 'aleatorio':
            define_atributos_aleatoriamente(personagem)
            break
        else:
            print(f'Desculpe, {resp} não é uma opção, escolha novamente.')

    personagem.imprime_atributos()



def altera_atributos(personagem):
    '''
    Esta função modifica os atributos anteriormente selecionados de acordo com a raça escolhida
    pelo usuário.
    '''

    lista_modificadores = []
    modificadores = personagem.raca.modificadores_atributos.split(', ') #['carisma 2', 'forca 1', 'escolhe 3',...]
    for modificador in modificadores:
        modificador = modificador.strip().split()
        modificador[1] = int(modificador[1])
        lista_modificadores.append(modificador) # [['carisma', 2], ['forca', 1], ['escolhe', 3]...]
    i = 0
    escolhidos = []
    while i < len(modificadores):

        if lista_modificadores[i][0] in nomes_atributos:
            personagem.atributos[lista_modificadores[i][0]].modificador += lista_modificadores[i][1]
            escolhidos.append(lista_modificadores[i][0])
            print(f'Seu modificador de {lista_modificadores[i][0]} agora é {personagem.atributos[lista_modificadores[i][0]].modificador}.')
        elif lista_modificadores[i][0] == 'escolhe':
            k = 0
            while k < lista_modificadores[i][1]:
                print(f'Escolha {lista_modificadores[i][1]-k} atributos nos quais deseja adicionar +1 em seu modificador: ')
                for nome_atributo in nomes_atributos:
                    if nome_atributo not in escolhidos:
                        print(f'-{nome_atributo}')
                atr = input()
                print()
                personagem.imprime_atributos()
                encontrou = False
                for nome_atributo in nomes_atributos:
                    if atr in formatacao(nome_atributo):
                        if nome_atributo in escolhidos:
                            print(f'O atributo {nome_atributo} já foi escolhido ou você não pode escolhe-lo, selecione outro {nomes_atributos}')
                        else:
                            escolhidos.append(nome_atributo)
                            k += 1
                            personagem.atributos[nome_atributo].modificador += 1
                            print(f'Agora seu modificador de {nome_atributo} é {personagem.atributos[nome_atributo].modificador}!')
                        encontrou = True
                        break
                if not encontrou:
                    print(f'{atr.title()} não é um atributo. Por favor digite novamente: ')
        i += 1
    personagem.imprime_atributos()


def alteracoes_raca(personagem):
    altera_atributos(personagem)


def escolhe_raca(personagem):
    nomes_racas, linhas = abre_arquivo('racas.txt')
    raca = Raca(habilidades=[])
    raca_escolhida = escolhe_categoria(Palavra('raça', 'raças'), nomes_racas, escolhidos_antes=[])[0]

    achou = False
    for linha in linhas:
        if not achou:
            if 'nome: ' + formatacao(raca_escolhida) in formatacao(linha):
                raca.nome = raca_escolhida
                achou = True
        else:
            if 'atributos: ' in linha.lower():
                raca.modificadores_atributos = linha.strip('Atributos:').strip().strip('\n')
            elif '---' in linha:
                break
            elif 'habilidades:' in linha.lower():
                continue
            else:
                habilidade_info = linha.split('. ', 1)
                habilidade = Habilidade(habilidade_info[0].strip(), habilidade_info[1].strip().strip('\n'))
                raca.habilidades.append(habilidade)
    personagem.raca = raca


    alteracoes_raca(personagem)


def alteracoes_classe(personagem):
    '''
    Esta função faz as alterações nos PVs e PMs do personagem de acordo com a classe escolhida.
    '''
    if personagem.PV.max == 0:
        personagem.PV.max += personagem.classe.PV + personagem.atributos['Constituição'].modificador + (personagem.nivel-1)*(personagem.classe.PV//4 + personagem.atributos['Constituição'].modificador)
        personagem.PV.atual = personagem.PV.max
    else:
        print('Parece que sua seu personagem já tem PVs! Alterações de classe não serão feitas!')
    if personagem.PM.max == 0:
        personagem.PM.max += personagem.nivel*(personagem.classe.PM)
        personagem.PM.atual = personagem.PM.max
    else:
        print('Parece que sua seu personagem já tem PMs! Alterações de classe não serão feitas!')

    # Perícias
    for pericia_classe in personagem.classe.pericias:
        personagem.pericias[pericia_classe[:-6].strip().title()].treinada = True


def escolhe_classe(personagem):
    nomes_classes, linhas = abre_arquivo('classes.txt')
    classe = Classe(pericias=[], proficiencias=[])
    classe_escolhida = escolhe_categoria(Palavra('classe', 'classes'), nomes_classes, escolhidos_antes=[])[0]

    achou = False
    nivel = 1
    habilidades_classe = []
    for linha in linhas:
        if not achou:
            if 'Classe: ' + classe_escolhida in linha:
                classe.nome = classe_escolhida
                achou = True
        else:
            if 'descricao: ' in linha.lower():
                classe.descricao = linha.strip('Descricao:').strip('\n').strip()
            elif 'atributo: ' in linha.lower():
                classe.atributo = linha.strip('Atributo:').strip('\n').strip().split(' ou ')
            elif 'pv: ' in linha.lower():
                classe.PV = int(linha.strip('PV:').strip('\n').strip())
            elif 'pm: ' in linha.lower():
                classe.PM = int(linha.strip('PM:').strip('\n').strip())
            elif 'pericias: ' in linha.lower():
                pericias = linha.strip('Pericias:').lower().strip('\n').strip().split(', ', 2)
                classe.escolhe_pericias(pericias)
            elif 'proficiencias: ' in linha.lower():
                classe.proficiencias = linha.strip('Proficiencias:').strip('\n').strip().split(', ')
            elif '---' in linha:
                break
            elif 'habilidades de classe:' in linha.lower():
                continue
            else:
                habilidades_classe.append(linha.strip(f'{nivel}-').strip('\n').strip().split(', '))
                nivel += 1
    classe.habilidades = habilidades_classe
    personagem.classe = classe
    alteracoes_classe(personagem)


def escolhe_beneficios(personagem, beneficios):
    beneficios = beneficios.split('; ')
    beneficios = beneficios[0].split(', ') + beneficios[1].split(', ')
    # beneficios[0] = beneficios[0].split(', ')
    # beneficios[1] = beneficios[1].split(', ')
    # for i in range(2):
    #     for j in range(len(beneficios[i])):
    #         if i == 0: beneficios[i][j] = beneficios[i][j] + ' (perícia)'
    #         else: beneficios[i][j] = beneficios[i][j] + ' (poder)'
    # beneficios = beneficios[0] + beneficios[1]

    escolhidas = []
    for pericia in nomes_pericias:
        if personagem.pericias[pericia].treinada:
            escolhidas.append(pericia)

    beneficios = escolhe_categoria(Palavra('benefício', 'benefícios'), beneficios, 2, escolhidas, genero=1)

    return beneficios


def escolhe_origem(personagem):
    '''
    
    '''
    nomes_origens, linhas = abre_arquivo('origens.txt')
    origem_escolhida = escolhe_categoria(Palavra('origem', 'origens'), nomes_origens, escolhidos_antes=[])[0]
    
    origem = Origem(beneficios=[], itens=[])
    achou = False
    for linha in linhas:
        if not achou:
            if 'origem: ' + origem_escolhida.lower() in linha.lower():
                origem.nome = origem_escolhida
                achou = True
        else:
            if 'beneficios: ' in formatacao(linha):
                origem.beneficios = escolhe_beneficios(personagem, linha[len('Beneficios: '):].strip().strip('\n'))
            elif 'itens:' in formatacao(linha):
                origem.itens.append(linha.strip('Itens:').strip().strip('\n'))
            elif '---' in linha:
                break
    
    for pericia in nomes_pericias:
        for beneficio in origem.beneficios:
            if beneficio in pericia:
                personagem.pericias[pericia].treinada = True

    personagem.origem = origem


def escolhe_divindade(personagem):
    devotos_obrigatorios = ['clerigo', 'druida', 'paladino']
    if personagem.classe.nome in devotos_obrigatorios:
        religioso = 'sim'
    else:
        religioso = formatacao(input('Você quer tornar-se um seguidor de alguma divindade? (SIM ou NÃO)\n'))

    if religioso in 'nao':
        print('Você optou por não seguir nenhuma religião. Toda vez que subir de nível você terá outra oportunidade de virar seguidor de alguma divindade.')
        return
    elif religioso in 'sim':
        devoto = False
        while not devoto:
            nomes_divindades, linhas = abre_arquivo('divindades.txt')
            divindade_escolhida = escolhe_categoria(Palavra('divindade', 'divindades'), nomes_divindades, escolhidos_antes=[])[0]

            divindade = Divindade(devotos=[], poderes=[])
            achou = False
            for linha in linhas:
                if not achou:
                    if 'divindade: ' + divindade_escolhida.lower() in linha.lower():
                        divindade.nome = divindade_escolhida
                        achou = True
                else:
                    if 'devotos: ' in formatacao(linha):
                        if personagem.raca.nome != 'humano' and personagem.classe.nome != 'clerigo':
                            devoto = personagem.divindade.verifica_devotos(personagem.raca.nome, personagem.classe.nome, linha.strip('Devotos:').lower().strip().strip('\n').strip('.').split(', '))
                            if not devoto:
                                break
                        else:
                            devoto = True
                        divindade.devotos = linha[len('Devotos: '):].lower().strip().strip('\n').strip('.').split(', ')
                    elif 'crencas e objetivos: ' in formatacao(linha):
                        divindade.crencas_objetivos = linha[len('Crenças e Objetivos: '):].strip().strip('\n')
                    elif 'simbolo sagrado: ' in formatacao(linha):
                        divindade.simbolo = linha[len('Símbolo Sagrado: '):].strip().strip('\n')
                    elif 'canalizar energia: ' in formatacao(linha):
                        divindade.energia = linha[len('Canalizar Energia: '):].strip().strip('\n')
                    elif 'arma preferida: ' in formatacao(linha):
                        divindade.arma = linha[len('Arma Preferida: '):].strip().strip('\n')
                    elif 'poderes concedidos: ' in formatacao(linha):
                        divindade.poderes.append(escolhe_categoria(Palavra('poder', 'poderes'), linha[len('Poderes Concedidos: '):].strip().strip('\n').strip('.').split(', '), escolhidos_antes = [], genero = 1)[0])
                    elif 'obrigacoes & restricoes' in formatacao(linha):
                        divindade.obrigacoes_restricoes = linha[len('Obrigações & Restrições: '):].strip().strip('\n')
                    elif '---' in linha:
                        break
                    
        personagem.divindade = divindade

    else:
        print(f'{religioso.title()} não é uma resposta válida!')
        escolhe_divindade()


def escolhe_pericias(personagem):
    n_pericias_escolher = max(personagem.atributos['Inteligência'].modificador, 0)
    if n_pericias_escolher:
        print(f'Como o seu modificador de inteligência é {personagem.atributos["Inteligência"].modificador}, você pode escolhe mais {personagem.atributos["Inteligência"].modificador} perícias para ser treinado.')
        pericias = escolhe_categoria(Palavra('perícia', 'perícias'), nomes_pericias, n_pericias_escolher, personagem.pericias_treinadas())
        for pericia in pericias:
            personagem.pericias[pericia].treinada = True
    
    # atribui valor de bônus às perícias
    for pericia in nomes_pericias:
        personagem.calcula_pericia(pericia)


def escolhas(personagem):
    define_atributos(personagem)
    escolhe_raca(personagem)
    personagem.raca.imprime()
    escolhe_classe(personagem)
    personagem.classe.imprime()
    escolhe_origem(personagem)
    personagem.origem.imprime()
    escolhe_divindade(personagem)
    if personagem.divindade.nome != '': personagem.divindade.imprime()
    escolhe_pericias(personagem)
    personagem.imprime_pericias()
    personagem.imprime()


def criar_personagem():
    nome = input('Digite o nome do seu personagem: ').title()
    jogador = input('Qual o nome do jogador desse personagem? ').title()
    print()
    personagem = Personagem(nome=nome, jogador=jogador, atributos=dicionario_atributos, pericias=dicionario_pericias)

    return personagem


def main():
    personagem = criar_personagem()
    escolhas(personagem)


if __name__ == "__main__":
    main()