from random import randint
from funcoes import *


'''
URGENTE:
-[X] Mover todas as funções para fora de Personagem() para poder criar um arquivo com apenas as classes
-[X] Criar método __init__ para criar pacote python
-[] Analisar bug em PM no fim
-[] Bug divindades onde pede para escolher entre poderes concedidos de outra divindade
-[X] Retirar código comentado em racas.py
-[] Bug de não conseguir modificar Defesa (outros) no PDF

Criação de Personagem:
01-[X] Definindo os 6 atributos: Forca, Destreza, Constituicao, Inteligencia, Sabedoria e Carisma
    -[] Refazer sistema de pontos para conseguir colocar: 'forca 4'/ 'for -1' e coisas do tipo em apenas 1 linha
    -[X] Sistema para escolher os atributos aleatoriamente
02-[X] Escolhendo raça: 17 raças que alteram atributos e adicionam habilidades
    -[X] Adquirir as infos de racas.txt para serem usadas
    -[X] Criar função que adiciona os modificadores de atributos da raça
    -[X] Criar uma função para cada habilidade (futuramente...)
    -[X] Criar excessão do golem não poder escolher origem e sim um poder geral
    -[] Falta Osteon e golem escolher poder
03-[X] Escolhendo classe: 14 classes
    -[X] Adquirir as infos de classes.txt para serem usadas
    -[X] Criar função que adiciona os PMs e PVs
    -[X] Adicionar perícias (futuramente...)
04-[X] Escolhendo origem: 35 origens
    -[X] Adquirir as infos de origens.txt para serem usadas
    -[X] Você escolhe dois benefícios da lista de benefícios -> fazer depois de implementar perícias
05-[X] Escolhendo divindade (opcional): 20 divindades
    -[X] Poder sair da escolha de divindades
    -[X] Descrição da divindade na lista de divindades
    -[X] Não mostrar as divindades que não podem ser escolhidas
    -[X] Adquirir as infos de divindades.txt para serem usadas 
    -[X] Apenas certas classes ou raças podem ser devotos de certas divindades
06-[X] Escolhendo Pericias: 30 perícias
    -[] Criar forma personalizada para a perícia Ofício
    -[X] Função que calcula o bônus de perícia
-[] Percebi que preciso todas as funções de raças e classes para continuar daqui em diante
    -[X] Funções raças prontas com excessões: escolha de magias, osteon, escolha de poderes
    -[] Funções classes
07-[] Anotando Equipamento Inicial: definido pela classe e origem
08-[X] Toques finais: PV, PM, ataques, nome, deslocamento, defesa, tamanho...
    -[X] Cálculo defesa
09-[] Salvar personagem criado em arquivo nome_personagem.pdf
10-[] Importar personagem em arquivos nome_personagem.pdf para um objeto dentro do programa
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
-[] implementar em todo o código a função de ignorar acentos -> falta nos atributos
'''


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


def adiciona_habilidades(personagem): # talvez percise usar isso pro OSTEON funcionar
    # for habilidade in personagem.raca.habilidades:
    #     nome_funcao = formatacao(habilidade.nome)
    #     if nome_funcao in funcoes_racas:
    #         funcao_executada = funcoes_racas[nome_funcao]
    #         funcao_executada(personagem)
    #     else:
    #         print(f'A função {nome_funcao} não existe :(')
    
    nome_funcao = formatacao(personagem.raca.nome)
    if nome_funcao in funcoes_racas:
        funcao_executada = funcoes_racas[nome_funcao]
        funcao_executada(personagem)
    else:
        print(f'A função {nome_funcao} não existe :(')


def alteracoes_raca(personagem):
    altera_atributos(personagem)
    adiciona_habilidades(personagem)
    personagem.modificadores_tamanho()


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

    # Proficiência
    personagem.proficiencias += personagem.classe.proficiencias


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
    '''beneficios[0] = beneficios[0].split(', ')
    beneficios[1] = beneficios[1].split(', ')
    for i in range(2):
        for j in range(len(beneficios[i])):
            if i == 0: beneficios[i][j] = beneficios[i][j] + ' (perícia)'
            else: beneficios[i][j] = beneficios[i][j] + ' (poder)'
    beneficios = beneficios[0] + beneficios[1]'''

    escolhidas = []
    for pericia in nomes_pericias:
        if personagem.pericias[pericia].treinada:
            escolhidas.append(pericia)

    beneficios = escolhe_categoria(Palavra('benefício', 'benefícios'), beneficios, 2, escolhidas, genero=1)

    return beneficios


def escolhe_origem(personagem):
    '''
    
    '''
    if formatacao(personagem.raca.nome) != 'golem':
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
                    if origem.nome != 'Amnésico': # provisório
                        origem.beneficios = escolhe_beneficios(personagem, linha[len('Beneficios: '):].strip().strip('\n'))
                    else: origem.beneficios.append(linha[len('Beneficios: '):].strip().strip('\n'))
                elif 'itens:' in formatacao(linha):
                    origem.itens.append(linha.strip('Itens:').strip().strip('\n'))
                elif '---' in linha:
                    break
        
        for pericia in nomes_pericias:
            for beneficio in origem.beneficios:
                if beneficio in pericia:
                    personagem.pericias[pericia].treinada = True

        personagem.origem = origem
    else:
        print('Por ser um golem você foi construído “pronto” para um propósito específico e não teve uma infância. Você não tem direito a escolher uma origem, mas recebe um poder geral a sua escolha.')
        # programar a parte de escolher poder


def divindades_aceitas(personagem):
    nomes_divindades, linhas = abre_arquivo('divindades.txt')
    divindades_aceitas = []
    for divindade in nomes_divindades:
        encontrou = False
        for linha in linhas:
            if 'Divindade: ' + divindade in linha:
                encontrou = True
                continue
            if encontrou:
                devotos = formatacao(linha[len('Devotos: '):]).strip().strip('\n').strip('.').split(', ')
                devoto = personagem.divindade.verifica_devotos(personagem.raca.nome, personagem.classe.nome, devotos)
                if devoto:
                    divindades_aceitas.append(divindade)
                break

    return divindades_aceitas


def cria_descricoes_divindades():
    nomes_divindades, linhas = abre_arquivo('divindades.txt')
    descricoes_divindades = []
    for linha in linhas:
        if 'Crenças e Objetivos:'.lower() in linha.lower():
            descricoes_divindades.append(linha[len('Crenças e Objetivos: '):linha.index('. ')+1])
    
    return descricoes_divindades


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
            descricoes_divindades = cria_descricoes_divindades()
            if formatacao(personagem.raca.nome) != 'humano' and formatacao(personagem.classe.nome) != 'clerigo':
                pode_ser_devoto = divindades_aceitas(personagem)
            else:
                pode_ser_devoto = nomes_divindades
            escolhida = False
            while not escolhida:
                print(f'\nEscolha 1 divindade dentre: ')
                i = 0
                for nome_divindade in nomes_divindades:
                    if nome_divindade in pode_ser_devoto:
                        print(f'-{nome_divindade.upper()}. {descricoes_divindades[i]} ')
                    i += 1
                divindade_escolhida = formatacao(input())
                if formatacao(divindade_escolhida) in 'sair':
                    print('Você optou por não seguir nenhuma religião. Toda vez que subir de nível você terá outra oportunidade de virar seguidor de alguma divindade.')
                    return
                encontrou = False
                for nome_divindade in nomes_divindades:
                    if divindade_escolhida in formatacao(nome_divindade):
                        if nome_divindade in pode_ser_devoto:
                            divindade_escolhida = nome_divindade
                            escolhida = True
                            print(f'Divindade escolhida: {nome_divindade.title()}')
                            encontrou = True
                            break
                        else:
                            print(f'{nome_divindade.title()} já foi escolhido!')
                            encontrou = True
                            break
                if not encontrou:
                    print(f'{divindade_escolhida.title()} não é um item válido!')


            divindade = Divindade(devotos=[], poderes=[])
            achou = False
            for linha in linhas:
                if not achou:
                    if 'divindade: ' + divindade_escolhida.lower() in linha.lower():
                        divindade.nome = divindade_escolhida
                        achou = True
                else:
                    if 'devotos: ' in formatacao(linha):
                        # if personagem.raca.nome != 'humano' and personagem.classe.nome != 'clerigo':
                        #     devoto = personagem.divindade.verifica_devotos(personagem.raca.nome, personagem.classe.nome, linha.strip('Devotos:').lower().strip().strip('\n').strip('.').split(', '))
                        #     if not devoto:
                        #         break
                        # else:
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
            personagem.adiciona_pericia(pericia)

    personagem.atualiza_pericias()


def escolhas(personagem):
    define_atributos(personagem)
    personagem.calcula_limite_carga()
    escolhe_raca(personagem)
    personagem.raca.imprime()
    escolhe_classe(personagem)
    personagem.classe.imprime()
    escolhe_pericias(personagem)
    escolhe_origem(personagem)
    personagem.origem.imprime()
    escolhe_divindade(personagem)
    personagem.atualiza_proficiencias()
    if personagem.divindade.nome != '': personagem.divindade.imprime()
    personagem.imprime_pericias()
    personagem.imprime()


def criar_personagem():
    nome = input('Digite o nome do seu personagem: ').title()
    jogador = input('Qual o nome do jogador desse personagem? ').title()
    print()
    personagem = Personagem(nome=nome, jogador=jogador, atributos=dicionario_atributos, pericias=dicionario_pericias)

    return personagem


def personagem_pdf(personagem):
    preencher_campos_selecao('fichas/ficha_base.pdf', atribui_personagem_pdf(personagem))


def input_personagem():
    
    while True:
        resp = formatacao(input('Como quer criar seu personagem? Pronto, Criar OU PDF\n'))
        if resp in 'pronto' or resp == '\n':
            return Personagem(nome='Nome Personagem', jogador='Nome Jogador', nivel=1, raca=Raca(nome='Trog', modificadores_atributos='Constituição 2, Força 1, Inteligência -1', habilidades=[Habilidade(nome='Mau Cheiro', descricao='Você pode gastar uma ação padrão e 2 PM para expelir um gás fétido. Todas as criaturas (exceto trogs) em alcance curto devem passar em um teste de Fortitude contra veneno (CD Con) ou ficarão enjoadas durante 1d6 rodadas. Uma criatura que passe no teste de resistência fica imune a esta habilidade por um dia.'), Habilidade(nome='Mordida', descricao='Você possui uma arma natural de mordida (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida.'), Habilidade(nome='Reptiliano', descricao='Você é uma criatura do tipo monstro e recebe visão no escuro, +1 na Defesa e, se estiver sem armadura ou roupas pesadas, +5 em Furtividade.'), Habilidade(nome='Sangue Frio', descricao='Você sofre 1 ponto de dano adicional por dado de dano de frio.')]), classe=Classe(nome='Paladino', descricao='Um campeão do bem e da ordem, o perfeito soldado dos deuses.', atributo=['Força', 'Carisma'], PV=20, PM=3, pericias=['luta (for)', 'vontade (sab)', 'cavalgar (des)', 'percepção (sab)'], proficiencias=['Armas marciais', 'armaduras pesadas', 'escudos'], habilidades=[['Abençoado', 'código do herói', 'golpe divino (+1d8)'], ['Cura pelas mãos (1d8+1 PV)', 'poder de paladino'], ['Aura sagrada', 'poder de paladino'], ['Poder de paladino'], ['Bênção da justiça', 'golpe divino (+2d8)', 'poder de paladino'], ['Cura pelas mãos (2d8+2 PV)', 'poder de paladino'], ['Poder de paladino'], ['Poder de paladino'], ['Golpe divino (+3d8)', 'poder de paladino'], ['Cura pelas mãos (3d8+3 PV)', 'poder de paladino'], ['Poder de paladino'], ['Poder de paladino'], ['Golpe divino (+4d8)', 'poder de paladino'], ['Cura pelas mãos (4d8+4 PV)', 'poder de paladino'], ['Poder de paladino'], ['Poder de paladino'], ['Golpe divino (+5d8)', 'poder de paladino'], ['Cura pelas mãos (5d8+5 PV)', 'poder de paladino'], ['Poder de paladino'], ['Poder de paladino', 'vingador sagrado']]), origem=Origem(nome='Minerador', beneficios=['Fortitude', 'Ataque Poderoso'], itens=['Gemas preciosas no valor de T$ 100, picareta']), divindade=Divindade(nome='Marah', crencas_objetivos='Praticar o amor e a gratidão pela vida e pela bondade. Promover a paz, harmonia e felicidade. Aliviar a dor e o sofrimento, trazer conforto aos aflitos. Praticar a caridade e o altruísmo. Oferecer clemência, perdão e redenção.', simbolo='Um coração vermelho.', energia='Positiva.', arma='Não há. Devotos desta deusa não podem lançar a magia Arma Espiritual e similares.', devotos=['suraggel (aggelus)', 'elfos', 'hynne', 'qareen', 'bardos', 'nobres', 'paladinos'], poderes=['Aura de Paz'], obrigacoes_restricoes='Devotos de Marah não podem causar dano, perda de PV e condições a criaturas, exceto enfeitiçado, fascinado e pasmo (fornecer bônus em dano também é proibido). Em combate, só podem recorrer a ações como proteger ou curar — ou fugir, render-se ou aceitar a morte. Um devoto de Marah jamais vai causar violência, nem mesmo para se salvar.'), atributos={'Força': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=1, descricao='Força (FOR): Seu poder muscular. A Força é aplicada em testes de Atletismo e Luta;\n                                 rolagens de dano corpo a corpo ou com armas de arremesso, e testes de Força\n                                 para levantar peso e atos similares.', pericias='Atletismo, Luta'), 'Destreza': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=-1, descricao='Destreza (DES): Sua agilidade, reflexos, equilíbrio e coordenação motora. A Destreza é                                 aplicada na Defesa e em testes de Acrobacia, Cavalgar, Furtividade, Iniciativa,                                 Ladinagem, Pilotagem, Pontaria e Reflexos.', pericias='Acrobacia, Cavalgar, Furtividade, Iniciativa, Ladinagem, Pilotagem, Pontaria, Reflexos'), 'Constituição': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=3, descricao='Constituição (CON): Sua saúde e vigor. A Constituição é aplicada aos pontos de vida                                 iniciais e por nível e em testes de Fortitude. Se a Constituição muda, seus pontos de vida                                 aumentam ou diminuem retroativamente de acordo.', pericias='Fortitude'), 'Inteligência': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=-1, descricao='Inteligência (INT): Sua capacidade de raciocínio, memória e educação.                                 A Inteligência é aplicada em testes de Conhecimento, Guerra, Investigação,                                 Misticismo, Nobreza e Ofício. Além disso, se sua Inteligência for positiva,                                 você recebe um número de perícias treinadas igual ao valor dela (não precisam ser                                 da sua classe).', pericias='Conhecimento, Guerra, Investigação, Misticismo, Nobreza, Ofício'), 'Sabedoria': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=-2, descricao='Sabedoria (SAB): Sua observação, ponderação e determinação. A Sabedoria é aplicada                                 em testes de Cura, Intuição, Percepção, Religião, Sobrevivência e Vontade.', pericias='Cura, Intuição, Percepção, Religião, Sobrevivência, Vontade'), 'Carisma': Atributo(valor_pontos=0, valor_rolamentos=10, modificador=1, descricao='Carisma (CAR): Sua força de personalidade e capacidade de persuasão, além de uma mistura de simpatia                                 e beleza. O Carisma é aplicado em testes de Adestramento, Atuação, Diplomacia,                                 Enganação, Intimidação e Jogatina.', pericias='Adestramento, Atuação, Diplomacia, Enganação, Intimidação, Jogatina')}, pericias={'Acrobacia': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Adestramento': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Atletismo': Pericia(atributo='Força', treinada=False, modificadores={}, modificador=1), 'Atuação': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Cavalgar': Pericia(atributo='Destreza', treinada=True, modificadores={}, modificador=1), 'Conhecimento': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Cura': Pericia(atributo='Sabedoria', treinada=False, modificadores={}, modificador=-2), 'Diplomacia': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Enganação': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Fortitude': Pericia(atributo='Constituição', treinada=True, modificadores={}, modificador=5), 'Furtividade': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Guerra': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Iniciativa': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Intimidação': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Intuição': Pericia(atributo='Sabedoria', treinada=False, modificadores={}, modificador=-2), 'Investigação': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Jogatina': Pericia(atributo='Carisma', treinada=False, modificadores={}, modificador=1), 'Ladinagem': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Luta': Pericia(atributo='Força', treinada=True, modificadores={}, modificador=3), 'Misticismo': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Nobreza': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Ofício': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=-1), 'Ofício 2': Pericia(atributo='Inteligência', treinada=False, modificadores={}, modificador=0), 'Percepção': Pericia(atributo='Sabedoria', treinada=True, modificadores={}, modificador=0), 'Pilotagem': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Pontaria': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Reflexos': Pericia(atributo='Destreza', treinada=False, modificadores={}, modificador=-1), 'Religião': Pericia(atributo='Sabedoria', treinada=False, modificadores={}, modificador=-2), 'Sobrevivência': Pericia(atributo='Sabedoria', treinada=False, modificadores={}, modificador=-2), 'Vontade': Pericia(atributo='Sabedoria', treinada=True, modificadores={}, modificador=0)}, proficiencias=['Armas marciais', 'armaduras pesadas', 'escudos'], caracteristicas=[Habilidade(nome='Reptiliano', descricao='Você é uma criatura do tipo monstro.'), Habilidade(nome='Visão no Escuro', descricao='Você vê no escuro.'), Habilidade(nome='Reptiliano 2', descricao='Se você estiver sem armadura ou roupas pesadas, +5 em Furtividade.'), Habilidade(nome='Sangue Frio', descricao='Você sofre 1 ponto de dano adicional por dado de dano de frio.')], habilidades_poderes=[Habilidade(nome='Mau Cheiro', descricao='Você pode gastar uma ação padrão e 2 PM para expelir um gás fétido. Todas as criaturas (exceto trogs) em alcance curto devem passar em um teste de Fortitude contra veneno (CD Con) ou ficarão enjoadas durante 1d6 rodadas. Uma criatura que passe no teste de resistência fica imune a esta habilidade por um dia.'), Habilidade(nome='Mordida', descricao='Você possui uma arma natural de mordida (dano 1d6, crítico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida.')], PV=Pontos(atual=23, max=23, temp=0, extra_nivel={}), PM=Pontos(atual=3, max=3, temp=0, extra_nivel={}), resistencias={}, fraquezas={'Frio': 1}, imunidades=[], defesa=Defesa(valor=10, modificadores={'Reptiliano': 1}), tamanho='Médio', furtividade_manobra=[0, 0], deslocamento=9, penalidade_armadura={}, equipamento=[])
        elif resp in 'criar':
            personagem = criar_personagem()
            escolhas(personagem)
            return personagem
        elif resp in 'pdf':
            print('Infelizmente ainda não foi implementado ;(')
            exit()
        else:
            print(f'{resp} não é uma resposta válida.')



def main():
    personagem = input_personagem()
    personagem_pdf(personagem)


if __name__ == "__main__":
    main()