from dataclasses import dataclass, field
from typing import DefaultDict
from random import randint
import os
import ast
from random import randint
import re

# paths
path = '/home/maraolt/Documents/projects/automatic_rpg_battles' # ubuntu desktop



'''
Criação de Personagem:
1-[X] Definindo os 6 atributos: Forca, Destreza, Constituicao, Inteligencia, Sabedoria e Carisma
    -[] Refazer sistema de pontos para conseguir colocar: 'forca 4'/ 'for -1' e coisas do tipo em apenas 1 linha
    -[X] Sistema para escolher os atributos aleatoriamente
2-[X] Escolhendo raça: 17 raças que alteram atributos e adicionam habilidades
    -[X] Adquirir as infos de racas.txt para serem usadas
    -[X] Criar função que adiciona os modificadores de atributos da raça
    -[] Criar uma função para cada habilidade (futuramente...)
3-[] Escolhendo classe: 14 classes
    -[X] Adquirir as infos de classes.txt para serem usadas
    -[] Criar função que adiciona os PMs e PVs
    -[] Adicionar perícias (futuramente...)
4-[] Escolhendo origem:
5-[] Escolhendo divindade (opcional):
6-[] Escolhendo Pericias
7-[] Anotando Equipamento Inicial: definido pela classe e origem
8-[] Toques finais: PV, PM, ataques, nome, deslocamento, defesa, tamanho...
9-[] Escolhendo magias: apenas 4 classes possuem magias (arcanista, bardo, clerigo e druida)

Anotações gerais:
-[] fazer comentarios nas funções
-[] verificar se tem lugares no código que necessitam de um 'break'
'''

nomes_atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']


#FUNÇÃO DOS DADOS
def rolagem(dado):
    resultado = 0
    dado = dado.split('d')
    for i in range(int(dado[0])):
        resultado += randint(1, int(dado[-1]))
    return resultado


def erro():
    print('Erro, tente novamente!')


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


# aqui eu vou escrever todas as habilidades em codigo
@dataclass
class Habilidade:
    nome: str = ''
    descricao: str = ''


    def print(self):
        print(f'-{self.nome.upper()}')
        if self.descricao is not None:
            print(self.descricao + '\n')


@dataclass
class Pontos:
    atual: int = 0
    max: int = 0
    temp: int = 0


@dataclass
class Raca:
    '''
    Objetos para todas as 17 raças existentes.
    '''
    nome: str = ''
    modificadores_atributos: str = ''
    habilidades: list = None



@dataclass
class Classe:
    '''
    Objeto para todas as 14 classes existentes.
    '''
    nome: str = ''
    descricao: str = ''
    atributo: list = None
    PV: int = 0
    PM: int = 0
    pericias: list = None
    proficiencias: list = None
    habilidades: list = None


    def escolhe_pericias(self, conj_pericias):

        pericias = []
        escolha = re.compile(r'^escolha (\d+) entre: ')
        escolhidos = []
        for conj_pericia in conj_pericias:
            if ' ou ' in conj_pericia:
                conj_pericia = conj_pericia.split(' ou ')
                while True:
                    resp = input(f'Em qual pericia você quer ser treinado? {conj_pericia[0]} ou {conj_pericia[1]}').lower()
                    if resp in conj_pericia:
                        pericias.append(resp)
                        break
                    else:
                        print(f'{resp} não é uma das opções. ', end='')
            elif escolha.match(conj_pericia):
                n_escolhas = int(escolha.match(conj_pericia).group(1))
                conj_pericia = conj_pericia[conj_pericia.index(':'):].strip('\n').strip().split(', ')
                i = 0
                
                while i < n_escolhas:
                    print(f'Escolha {n_escolhas-i} perícias dentre: ')
                    for pericia in conj_pericia:
                        if pericia not in escolhidos:
                            print(f'-{pericia}')
                    resp = input('\n')
                    if resp in conj_pericia:
                        if resp not in escolhidos:

                        else:
                            print(f'Esta perícia já foi escolhida!')
                    else:
                        print(f'{resp} não é uma perícia válida!')
                    







dicionario_atributos = {'forca': Atributo(0, 10, 0, '''Força (FOR): Seu poder muscular. A Força é aplicada em testes de Atletismo e Luta;
                                 rolagens de dano corpo a corpo ou com armas de arremesso, e testes de Força
                                 para levantar peso e atos similares.''',\
                                      'Atletismo, Luta'), \
                'destreza': Atributo(0, 10, 0, 'Destreza (DES): Sua agilidade, reflexos, equilíbrio e coordenação motora. A Destreza é\
                                 aplicada na Defesa e em testes de Acrobacia, Cavalgar, Furtividade, Iniciativa,\
                                 Ladinagem, Pilotagem, Pontaria e Reflexos.',\
                                      'Acrobacia, Cavalgar, Furtividade, Iniciativa, Ladinagem, Pilotagem, Pontaria, Reflexos'), \
                'constituicao': Atributo(0, 10, 0, 'Constituição (CON): Sua saúde e vigor. A Constituição é aplicada aos pontos de vida\
                                 iniciais e por nível e em testes de Fortitude. Se a Constituição muda, seus pontos de vida\
                                 aumentam ou diminuem retroativamente de acordo.',\
                                      'Fortitude'), \
                'inteligencia': Atributo(0, 10, 0, 'Inteligência (INT): Sua capacidade de raciocínio, memória e educação.\
                                 A Inteligência é aplicada em testes de Conhecimento, Guerra, Investigação,\
                                 Misticismo, Nobreza e Ofício. Além disso, se sua Inteligência for positiva,\
                                 você recebe um número de perícias treinadas igual ao valor dela (não precisam ser\
                                 da sua classe).',\
                                      'Conhecimento, Guerra, Investigação, Misticismo, Nobreza, Ofício'), \
                'sabedoria': Atributo(0, 10, 0, 'Sabedoria (SAB): Sua observação, ponderação e determinação. A Sabedoria é aplicada\
                                 em testes de Cura, Intuição, Percepção, Religião, Sobrevivência e Vontade.',\
                                      'Cura, Intuição, Percepção, Religião, Sobrevivência, Vontade'), \
                'carisma': Atributo(0, 10, 0, 'Carisma (CAR): Sua força de personalidade e capacidade de persuasão, além de uma mistura de simpatia\
                                 e beleza. O Carisma é aplicado em testes de Adestramento, Atuação, Diplomacia,\
                                 Enganação, Intimidação e Jogatina.',\
                                      'Adestramento, Atuação, Diplomacia, Enganação, Intimidação, Jogatina')}
raca_default = Raca('', '', '')
classe_default = Classe('', '', [], 0, 0, [], [], [])
pontos_default = Pontos(0, 0, 0)

@dataclass
class Personagem:
    nome: str = ''
    jogador: str = ''
    nivel: int = 1
    raca: Raca() = raca_default
    classe: Classe() = classe_default
    origem: str = ''
    divindade: str = ''
    atributos: DefaultDict[str, Atributo] = field(default_factory=dict)
    PV: Pontos() = pontos_default
    PM: Pontos() = pontos_default
    defesa: int = 0


    def imprime(self):
        print(f'{self.nome} ({self.jogador})')
        print(f'{self.classe}/{self.raca} {self.nivel}')


    def define_atributos_pontos(self):
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
            self.imprime_atributos()
            print('Para sair desta função escreva: "sair".')
            atr = input('Escolha um atributo (for, des, con, int, sab, car): ').lower()
            if atr == 'sair':
                if pontos != 0:
                    print('Você ainda não pode sair, pois deve gastar todos os pontos (positivos e/ou negativos).')
                else:
                    break
            for nome_atributo in nomes_atributos:
                if atr in nome_atributo:
                    while True:
                        try:
                            pontos_usados = int(input(f'Você possui {pontos} pontos. Quantos pontos deseja gastar em {nome_atributo}? '))
                            if pontos_usados > 7 or pontos_usados < -1:
                                print('O número de pontos usado em um atributo deve ser no máximo 7 e no mínimo -1. Tente novamente.')
                                continue
                            self.atributos[nome_atributo].valor_pontos = pontos_usados
                            modificador = self.atributos['forca'].calcula_modificador_pontos(pontos_usados)
                            self.atributos[nome_atributo].modificador = modificador
                            pontos_gastos = sum(atributo.valor_pontos for atributo in self.atributos.values())
                            pontos = 10 - pontos_gastos
                            print(f'Seu modificador de {nome_atributo} é {modificador} e você possui mais {pontos} pontos.')
                            break
                        except ValueError:
                            erro()


    def rolagens_atributos(self):
        todas_rolagens = []
        for _ in range(6):
            rolagens_somadas = []
            for _ in range(4):
                rolagens_somadas.append(rolagem('1d6'))
            rolagens_somadas = sorted(rolagens_somadas)
            todas_rolagens.append(sum(rolagens_somadas[1:]))
        todas_rolagens = sorted(todas_rolagens, reverse=True)

        return todas_rolagens


    def define_atributos_rolagens(self):
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
        
        todas_rolagens = self.rolagens_atributos()
        lista_modificadores = self.atributos['forca'].calcula_modificador_rolagens(todas_rolagens)

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
                    if atr in nome_atributo:
                        if nome_atributo not in escolhidos:
                            escolhidos.append(nome_atributo)
                            self.atributos[nome_atributo].valor_rolamentos = todas_rolagens[i]
                            self.atributos[nome_atributo].modificador = lista_modificadores[i]
                            for escolhido in escolhidos:
                                print(f'{escolhido}: {self.atributos[escolhido].modificador}')

                            i += 1
                        else:
                            print(f'Você já escolheu o atributo {nome_atributo}, por favor escolha outro ainda não escolhido.')
            except ValueError:
                erro()
        
        print('Todos os atributos foram escolhidos.')


    def define_atributos_manualmente(self):
        '''
        Esta funcao deixa o usuario definir os atributos manualmente
        '''

        print('Aqui voce colocara os atributos manualmente.')

        i = 0
        while i < len(nomes_atributos):
            try:
                atr = int(input(f'Qual o modificador de {nomes_atributos[i]}?\n'))
                self.atributos[nomes_atributos[i]].modificador = atr
                i += 1
                for j in range(i):
                    print(f'-{nomes_atributos[j]}: {self.atributos[nomes_atributos[j]].modificador}')

            except ValueError:
                erro()


    def define_atributos_aleatoriamente(self):
        todas_rolagens = self.rolagens_atributos()
        lista_modificadores = self.atributos['forca'].calcula_modificador_rolagens(todas_rolagens)
        escolhido = []
        n_modificador = 0
        while n_modificador < len(nomes_atributos):
            aleatorio = randint(0, 5)
            if nomes_atributos[aleatorio] not in escolhido:
                self.atributos[nomes_atributos[aleatorio]].modificador = lista_modificadores[n_modificador]
                n_modificador += 1
        print('Pronto! Seus atributos foram aleatoriamente gerados e distribuidos.')


    def define_atributos(self):
        '''
        Esta função simplesmente pergunta ao usuário qual das duas maneiras de definir os atributos básicos 
        ele prefere usar (pontos ou rolagens) e direciona-o para a respectiva função dependendo de sua resposta.
        '''
        while True:
            resp = input('Há quatro maneiras de definir seus atributos: com pontos, rolagens, manualmente ou aleatório. Escolha a que preferir: (Pontos OU Rolagens OU Manualmente OU Aleatorio)\n').lower()
            if resp in 'pontos' or 'pontos' in resp:
                self.define_atributos_pontos()
                break
            elif resp in 'rolagens' or resp in 'rolagem' or 'rolagens' in resp or 'rolagem' in resp:
                self.define_atributos_rolagens()
                break
            elif resp in 'manualmente':
                self.define_atributos_manualmente()
                break
            elif resp in 'aleatorio':
                self.define_atributos_aleatoriamente()
                break
            else:
                print(f'Desculpe, {resp} não é uma opção, escolha novamente.')

        self.imprime_atributos()


    def imprime_atributos(self):
        '''
        Esta função simplesmente imprime no terminal todos os atributos do personagem e seus respectivos modificadores.
        '''
        print('\nAtributos:')
        for nome_atributo in nomes_atributos:
            print(f'-{nome_atributo}: {self.atributos[nome_atributo].modificador}')
        print()


    def altera_atributos(self):

        lista_modificadores = []
        modificadores = self.raca.modificadores_atributos.split(', ') #['carisma 2', 'forca 1', 'escolhe 3',...]
        for modificador in modificadores:
            modificador = modificador.strip().split()
            modificador[1] = int(modificador[1])
            lista_modificadores.append(modificador) # [['carisma', 2], ['forca', 1], ['escolhe', 3]...]
        i = 0
        escolhidos = []
        while i < len(modificadores):

            if lista_modificadores[i][0] in nomes_atributos:
                self.atributos[lista_modificadores[i][0]].modificador += lista_modificadores[i][1]
                escolhidos.append(lista_modificadores[i][0])
                print(f'Seu modificador de {lista_modificadores[i][0]} agora é {self.atributos[lista_modificadores[i][0]].modificador}.')
            elif lista_modificadores[i][0] == 'escolhe':
                k = 0
                while k < lista_modificadores[i][1]:
                    atr = input(f'Escolha {lista_modificadores[i][1]-k} atributos nos quais deseja adicionar +1 em seu modificador {nomes_atributos}: ')
                    self.imprime_atributos()
                    for nome_atributo in nomes_atributos:
                        if atr in nome_atributo:
                            if nome_atributo in escolhidos:
                                print(f'O atributo {nome_atributo} já foi escolhido ou você não pode escolhe-lo, selecione outro {nomes_atributos}')
                            else:
                                escolhidos.append(nome_atributo)
                                k += 1
                                self.atributos[nome_atributo].modificador += 1
                                print(f'Agora seu modificador de {nome_atributo} é {self.atributos[nome_atributo].modificador}!')
                            break
                        # else:
                        #     print(f'{atr} não é um atributo. Por favor digite novamente: ')
            i += 1
        self.imprime_atributos()


    def alteracoes_raca(self):
        self.altera_atributos()


    def escolhe_raca(self):
        with open(os.path.join(path, 'racas.txt')) as arquivo:
            try:
                nomes_racas = ast.literal_eval(arquivo.readline())
            except ValueError:
                print("malformed string; skipping this line")
            except SyntaxError:
                print("looks like some encoding errors with this file...")
            linhas = arquivo.readlines()
        
        print('Escolha a sua raça dentre: ')
        for nome_raca in nomes_racas:
            print(f'-{nome_raca}')
        print()


        achou = False
        raca = Raca(habilidades=[])
        while True:
            raca_escolhida = input().lower()
            if raca_escolhida in nomes_racas:
                break
            else:
                print(f'{raca_escolhida} não é uma raça existente, tente novamente.')


        for linha in linhas:
            if not achou:
                if 'nome: ' + raca_escolhida in linha.lower():
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
        self.raca = raca


        self.alteracoes_raca()
        

    def imprime_raca(self):
        print('-'*40)
        print(self.raca.nome.title())
        print(f'Atributos: {self.raca.modificadores_atributos}\n')
        for habilidade in self.raca.habilidades:
            habilidade.print()
        print('-'*40)


    def alteracoes_classe(self):
        '''
        Esta função faz as alterações nos PVs e PMs do personagem de acordo com a classe escolhida.
        '''
        if self.PV.max == 0:
            self.PV.max += self.classe.PV + self.atributo['constituicao'].modifciador + (self.nivel-1)*(self.classe.PV//4 + self.atributos['consitituicao'].modificador)
            self.PV.atual = self.PV.max
        else:
            print('Parece que sua seu personagem já tem PVs! Alterações de classe não serão feitas!')
        if self.PM.max == 0:
            self.PM.max += self.nivel*(self.classe.PM)
            self.PM.atual = self.PM.max
        else:
            print('Parece que sua seu personagem já tem PMs! Alterações de classe não serão feitas!')


    def escolhe_classe(self):
        with open(os.path.join(path, 'classes.txt')) as arquivo:
            try:
                nomes_classes = ast.literal_eval(arquivo.readline())
            except ValueError:
                print("malformed string; skipping this line")
            except SyntaxError:
                print("looks like some encoding errors with this file...")
            linhas = arquivo.readlines()
            
        print('Escolha a sua classe dentre: ')
        for nome_classe in nomes_classes:
            print(f'-{nome_classe}')
        print()

        achou = False
        classe = Classe(pericias=[], proficiencias=[])
        while True:
            classe_escolhida = input().lower()
            if classe_escolhida in nomes_classes:
                break
            else:
                print(f'{classe_escolhida} não é uma classe existente, tente novamente.')


        nivel = 1
        habilidades_classe = []
        for linha in linhas:
            if not achou:
                if 'classe: ' + classe_escolhida in linha.lower():
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
                    pericias = linha.strip('Pericias:').strip('\n').strip().split(', ', 2)
                    # escolhe_pericias() # fazer essa função depois das pericias
                    classe.escolhe_pericias(pericias)
                    classe.pericias = pericias
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
        
        





        self.classe = classe
        self.alteracoes_classe()


    def imprime_classe(self):
        print('-'*40)
        # r = Classe()
        print(self.classe.nome.upper())
        print(self.classe.descricao)
        if len(self.classe.atributo) > 1:
            print(f'\nOs atributos mais importantes para essa classe são: {self.classe.atributo}')
        else:
            print(f'\nO atributo mais importante para essa classe é: {self.classe.atributo}')
        print(f'PV: {self.classe.PV} + Constituição ({self.classe.PV//4} por nível)')
        print(f'PM: {self.classe.PM} ({self.classe.PM} por nível)')
        print(f'Perícias: {self.classe.pericias}')
        print(f'Proficiências: {self.classe.proficiencias}')
        print(f'Habilidades de Classe: ')
        i = 1
        for habilidade in self.classe.habilidades:
            print(f'{i}- {habilidade}')
            i += 1
        print('-'*40)

# melhor usar como dicionario e fazer uma classe chamada 'pericia'
# class Pericias:
#     def __init__(self) -> None:
#         self.acrobacia = acrobacia
#         self.adestramento = adestramento
#         self.atletismo = atletismo
#         self.atuacao = atuacao
#         self.cavalgar = cavalgar
#         self.conhecimento = conhecimento
#         self.cura = cura
#         self.diplomacia = diplomacia
#         self.enganacao = enganacao
#         self.fortitude = fortitude
#         self.furtividade = furtividade
#         self.guerra = guerra
#         self.iniciativa = iniciativa
#         self.intimidacao = intimidacao
#         self.intuicao = intuicao
#         self.investigacao = investigacao
#         self.jogatina = jogatina


def criar_personagem():
    nome = input('Digite o nome do seu personagem: ')
    jogador = input('Qual o nome do jogador desse personagem? ')
    print()
    personagem = Personagem(nome=nome, jogador=jogador, atributos=dicionario_atributos)

    return personagem


def main():
    # gustavo = Personagem(nome='Doende Mardito', jogador='Gustavo', nivel=1, atributos=dicionario_atributos)
    personagem = criar_personagem()
    personagem.define_atributos()
    # personagem.escolhe_raca()
    # personagem.imprime_raca()
    # personagem.escolhe_classe()
    # personagem.imprime_classe()
    # gustavo.imprime_atributos()



main()