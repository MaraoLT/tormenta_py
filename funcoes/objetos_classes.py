from dataclasses import dataclass, field
from typing import DefaultDict
import re
from .basicas import *


@dataclass
class Palavra:
    singular: str = ''
    plural: str = ''


# ATRIBUTO
nomes_atributos = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']

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

# PERÍCIA
nomes_pericias = ['Acrobacia', 'Adestramento', 'Atletismo', 'Atuação', 'Cavalgar', 'Conhecimento', 
                        'Cura', 'Diplomacia', 'Enganação', 'Fortitude', 'Furtividade',
                        'Guerra', 'Iniciativa', 'Intimidação', 'Intuição', 'Investigação', 'Jogatina',
                        'Ladinagem', 'Luta', 'Misticismo', 'Nobreza', 'Ofício', 'Percepção',
                        'Pilotagem', 'Pontaria', 'Reflexos', 'Religião', 'Sobrevivência', 'Vontade']
penalidade_treino = ['Adestramento', 'Atuação', 'Conhecimento', 'Guerra', 'Jogatina', 'Ladinagem',
                      'Misticismo', 'Nobreza', 'Ofício', 'Pilotagem', 'Religião']
penalidade_armadura = ['Acrobacia', 'Furtividade', 'Ladinagem']

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

# Oficios: armeiro, alquimista, cozinheiro, alfaiate, carpinteiro, pedreiro, ourives, 
# fazendeiro, pescador, estalajadeiro, escriba, escultor, pintor


# @dataclass
# class Magia:
    

@dataclass
class Defesa:
    valor: int = 10
    modificadores: DefaultDict[str, int] = field(default_factory=dict)


    def calcula(self, destreza):
        soma_modificadores = 0
        for modificador in self.modificadores.values():
            soma_modificadores += modificador

        self.valor = 10 + soma_modificadores + destreza 


    def imprime(self, destreza):
        self.calcula(destreza)
        print(f'Defesa: {self.valor} (10 + {destreza} (des) + {self.modificadores})')


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
    extra_nivel: DefaultDict[str, int] = field(default_factory=dict)


    def imprime(self, texto):
        print(f'{texto}: {self.atual}/{self.max}')


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
        Esta função simplesmente imprime as características que a raça adiciona
        '''
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
        
        # print(f'Infelizmente você não pode ser devoto dessa divindade, pois apenas {devotos} podem ser devotos.')
        return False


    def imprime(self):
        '''
        Esta função simplesmente imprime as características que a divindade adiciona
        '''
        print(self.nome.upper())
        print(f'Crenças e Objetivos: {self.crencas_objetivos}\n')
        print(f'Símbolo Sagrado: {self.simbolo}\n')
        print(f'Energia: {self.energia}\n')
        print(f'Arma Preferida: {self.arma}\n')
        print(f'Devotos: {self.devotos}\n')
        print(f'Poderes Concedidos: {self.poderes}\n')
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
    proficiencias: list = field(default_factory=list)
    caracteristicas: list = field(default_factory=list)
    habilidades_poderes: list = field(default_factory=list)
    PV: Pontos = field(default_factory=Pontos)
    PM: Pontos = field(default_factory=Pontos)
    resistencias: DefaultDict[str, int] = field(default_factory=dict)
    fraquezas: DefaultDict[str, int] = field(default_factory=dict)
    imunidades: list = field(default_factory=list)
    defesa: Defesa = field(default_factory=Defesa)
    tamanho: str = 'Médio'
    deslocamento: int = 9 # em metros
    penalidade_armadura: DefaultDict[str, int] = field(default_factory=dict)
    equipamento: list = field(default_factory=list)


    def imprime(self):
        '''
        Imprime as informações básicas do personagem criado
        '''
        print()
        print(f'{self.nome} ({self.jogador})')
        print(f'{self.raca.nome.title()}/{self.classe.nome.title()} {self.nivel}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Deslocamento: {self.deslocamento}m')
        print(f'Resistências: {self.resistencias}')
        print(f'Fraquezas: {self.fraquezas}')
        print(f'Imunidades: {self.imunidades}\n')
        print(f'Proficiências: {self.proficiencias}\n')
        self.PV.imprime('PV')
        self.PM.imprime('PM')
        self.defesa.imprime(self.atributos['Destreza'].modificador)
        self.imprime_atributos()
        self.imprime_pericias()
        self.imprime_caracteristicas()
        self.imprime_habilidades_poderes()
        self.raca.imprime()
        self.classe.imprime()
        self.origem.imprime()
        if self.divindade.nome != '': self.divindade.imprime()


    def imprime_caracteristicas(self):
        '''
        Esta função simplesmente imprime as características do personagem
        '''
        print('CARACTERÍSTICAS:')
        for caracteristica in self.caracteristicas:
            caracteristica.imprime()
        print('-'*40)


    def imprime_habilidades_poderes(self):
        '''
        Esta função simplesmente imprime as características do personagem
        '''
        print('HABILIDADES E PODERES:')
        for habili_poderes in self.habilidades_poderes:
            habili_poderes.imprime()
        print('-'*40)


    def imprime_pericias(self):
        print('PERÍCIAS: ')
        for pericia in nomes_pericias:
            print(f'{pericia} ({self.pericias[pericia].atributo[:3]}): {self.pericias[pericia].modificador} {"(T)" if self.pericias[pericia].treinada else ""}')
        print('-'*40)


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
        for modificador in self.pericias[pericia].modificadores.values():
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


    def adiciona_pericia(self, pericia):
        self.pericias[pericia].treinada = True
        self.calcula_pericia(pericia)


    def atualiza_pericias(self):
        # atribui valor de bônus às perícias
        for pericia in nomes_pericias:
            self.calcula_pericia(pericia)


    def imprime_atributos(self):
        '''
        Esta função simplesmente imprime no terminal todos os atributos do personagem e seus respectivos modificadores.
        '''
        print('\nAtributos:')
        for nome_atributo in nomes_atributos:
            print(f'-{nome_atributo}: {self.atributos[nome_atributo].modificador}')
        print('-'*40)
