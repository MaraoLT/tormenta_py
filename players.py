from dataclasses import dataclass, field
from typing import DefaultDict
from random import randint
import os
import ast


'''
Criação de Personagem:
1-[X] Definindo os 6 atributos: Forca, Destreza, Constituicao, Inteligencia, Sabedoria e Carisma
2-[] Escolhendo raça: 17 raças que alteram atributos e adicionam habilidades
3-[] Escolhendo classe: 14 classes
4-[] Escolhendo origem:
5-[] Escolhendo divindade (opcional):
6-[] Escolhendo Pericias
7-[] Anotando Equipamento Inicial: definido pela classe e origem
8-[] Escolhendo magias: apenas 4 classes possuem magias (arcanista, bardo, clerigo e druida)
9-[] Toques finais: PV, PM, ataques, nome, deslocamento, defesa, tamanho...

Anotações gerais:
-[X] fazer comentarios na funcoes
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
        if pontos_gastos in [-1, 0, 1, 2]:
            return pontos_gastos
        elif pontos_gastos == 3:
            return 2
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


@dataclass
class Personagem:
    nome: str = ''
    jogador: str = ''
    nivel: int = 1
    raca: str = ''
    classe: str = ''
    origem: str = ''
    divindade: str = ''
    atributos: DefaultDict[str, Atributo] = field(default_factory=dict)
    PV_MAX: int = 0
    PV: int = 0
    PM_MAX: int = 0
    PM: int = 0
    defesa: int = 0
    # self.pericias = self.Pericias()


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
        
        todas_rolagens = []
        for _ in range(6):
            rolagens_somadas = []
            for _ in range(4):
                rolagens_somadas.append(rolagem('1d6'))
            rolagens_somadas = sorted(rolagens_somadas)
            todas_rolagens.append(sum(rolagens_somadas[1:]))
        todas_rolagens = sorted(todas_rolagens, reverse=True)

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
                            print(f'{nome_atributo}: {self.atributos[nome_atributo].modificador}')
                            i += 1
                        else:
                            print(f'Você já escolheu o atributo {nome_atributo}, por favor escolha outro ainda não escolhido.')
            except ValueError:
                erro()
        
        print('Todos os atributos foram escolhidos.')
        self.imprime_atributos()

        


    def define_atributos(self):
        '''
        Esta função simplesmente pergunta ao usuário qual das duas maneiras de definir os atributos básicos 
        ele prefere usar (pontos ou rolagens) e direciona-o para a respectiva função dependendo de sua resposta.
        '''
        while True:
            resp = input('Há duas maneiras de definir seus atributos: com pontos ou com rolagens. Escolha a que preferir: (Pontos OU Rolagens)\n').lower()
            if resp in 'pontos' or 'pontos' in resp:
                self.define_atributos_pontos()
                break
            elif resp in 'rolagens' or resp in 'rolagem' or 'rolagens' in resp or 'rolagem' in resp:
                self.define_atributos_rolagens()
                break
            else:
                print(f'Desculpe, {resp} não é uma opção, escolha novamente.')


    def imprime_atributos(self):
        '''
        Esta função simplesmente imprime no terminal todos os atributos do personagem e seus respectivos modificadores.
        '''
        print('\nAtributos:')
        for nome_atributo in nomes_atributos:
            print(f'-{nome_atributo}: {self.atributos[nome_atributo].modificador}')
        print()











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



# class Classe:
#     def __init__(self,):
#         self.arcanista = arcanista
#         self.barbaro = barbaro
#         self.bardo = bardo
#         self.bucaneiro = bucaneiro
#         self.cacador = cacador
#         self.cavaleiro = cavaleiro
#         self.clerigo = clerigo
#         self.druida = druida
#         self.guerreiro = guerreiro
#         self.inventor = inventor
#         self.ladino = ladino
#         self. lutador = lutador
#         self.nobre = nobre
#         self.paladino = paladino


def main():
    gustavo = Personagem('Doende Mardito', 'Gustavo', 1, 'goblin', 'bucaneiro', atributos=dicionario_atributos)
    gustavo.imprime()
    gustavo.define_atributos()
    # gustavo.imprime_atributos()



main()