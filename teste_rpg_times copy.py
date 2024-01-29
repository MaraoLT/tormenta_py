#TESTE RPG Times
# Escrita de personagem:
# {'nome':'nome', 'PV': 0, 'defesa': 0, 'ataque': 0, 'forca': 0, 'agilidade': 0, 'dano': '0d0', 'time': 'time'}
###
# A fazer:
# -Criticos e Nulos - V
# -Mais opções de ataques (mínimo 2)
# -Falas de morte
# -Contador de kills V
# -Número médio de rodadas
# -Cura
# -Adicionar armas
###
#OBS: precisei trocar a verificação de vitória para o início do while, diferentemente do que fiz nos outros
###
from random import randint
import os
import ast

texto = False
cont_rodadas = False
casos_teste = 10000
if casos_teste == 1:
    texto = True

#FUNÇÃO DOS DADOS
def rolagem(dado):
    resultado = 0
    dado = dado.split('d')
    for i in range(int(dado[0])):
        resultado += randint(1, int(dado[-1]))
    return resultado


#INICIATIVAS
def iniciativa():
    for i in range(num_personagens):
        personagens[i]['iniciativa'] = rolagem('1d20')+int(personagens[i]['agilidade'])
    personagens_iniciativa = sorted(personagens, key=lambda d: d['iniciativa'], reverse=True)
    return personagens_iniciativa


#GOLPES
def golpe(atacante, defensor):
    margem_critico = 20 # para personalizar críticos futuramente
    d20 = rolagem('1d20')
    if d20 <= 1:
        golpe = 0
        if texto: print(atacante['nome']+' errou MUITO o golpe em '+defensor['nome'])
        return golpe
    elif d20 >= margem_critico:
        golpe = rolagem(atacante['dano']) + rolagem(atacante['dano']) + int(atacante['forca'])
        if texto: print(atacante['nome']+' acertou um golpe CRITICO em '+defensor['nome']+' de '+str(golpe)+' de dano')
        return golpe
    else:
        ataque = d20 + int(atacante['forca'])
        defesa = defensor['defesa']
        if ataque >= defesa:
            golpe = rolagem(atacante['dano']) + int(atacante['forca'])
            if texto: print(atacante['nome']+' acertou o golpe em '+defensor['nome']+' de '+str(golpe)+' de dano')
        else:
            golpe = 0
            if texto: print(atacante['nome']+' errou o golpe em '+defensor['nome'])
        return golpe


#ALVOS
def alvos(num_atacante):
    alvo = randint(0, (num_personagens-1))
    if alvo != num_atacante and personagens[alvo]['vivo'] and personagens[num_atacante]['time'] != personagens[alvo]['time']:
        return alvo
    else:
        alvo = alvos(num_atacante)
        return alvo


#LEITURA DO ARQUIVO
# path = "/Users/Ainaras/Programação/Programação/Minhas ideias/RPG" # PC em Marília
path = "/run/media/ra182338/USB DISK/programas" # PC no IC
with open(os.path.join(path, 'personagens_times.txt')) as arquivo:
    linhas = arquivo.readlines()
# if there are irregularities, use a try/except to pass these (note, you may wish to use a logger in practice)    
personagens = []
for linha in linhas:
    try:
        personagens.append(ast.literal_eval(linha))
    except ValueError:
        print("malformed string; skipping this line")
    except SyntaxError:
        print("looks like some encoding errors with this file...")
 
num_personagens = len(personagens)
#adicionando 'vitorias', estado de ''vivo', 'elimininações' e salvado 'PVs' dos personagens
#print(personagens)
PVs = {}
for personagem in personagens:
    PVs[personagem['nome']] = personagem['PV']
    personagem['vitorias'] = 0  
    personagem['vivo'] = True
    personagem['eliminacoes'] = 0
rodada_max = 0
rodada_min = 100000
###BATALHA##
for j in range(casos_teste):
    rodada = 1
    for personagem in personagens:
        personagem['PV'] = PVs[personagem['nome']]
        personagem['vivo'] = True
    personagens = iniciativa()
    if texto: 
        for personagem in personagens: print(personagem['nome']+' iniciativa: '+str(personagem['iniciativa']))
        print('')
    while True:
        ######
        times_vivos = 0
        time = ''
        time_vencedor = ''
        for personagem in personagens:
            if time != personagem['time']:
                time = personagem['time']
                times_vivos+=1
                time_vencedor = personagem['time']
        # print(times_vivos)
        if times_vivos <= 1:
            for personagem in personagens:
                if personagem['time'] == time_vencedor:
                    personagem['vitorias'] += 1
            break
        ######
        if texto: print(f'Rodada {rodada}:')
        for i in range(num_personagens):
            if personagens[i]['vivo']:
                alvo = alvos(i)
                personagens[alvo]['PV'] -= golpe(personagens[i], personagens[alvo])
                if personagens[alvo]['PV'] <= 0:
                    #vencedor = personagens[i]['nome']
                    #personagens[i]['vitorias']+=1
                    personagens[alvo]['PV'] = 0
                    personagens[i]['eliminacoes'] += 1
                    personagens[alvo]['vivo'] = False

                    times_vivos = 0
                    time = ''
                    time_vencedor = ''
                    for personagem in personagens:
                        if personagem['vivo']:
                            if time != personagem['time']:
                                time = personagem['time']
                                times_vivos+=1
                                time_vencedor = personagem['time']
                    # print(times_vivos)
                    if times_vivos <= 1:
                        for personagem in personagens:
                            if personagem['time'] == time_vencedor:
                                personagem['vitorias'] += 1
                        break

                    if texto: print(personagens[alvo]['nome']+' morreu para '+personagens[i]['nome'])
                    #break;
        if texto:
            for personagem in personagens: print(personagem['nome']+' PV: '+str(personagem['PV']))
            print('')
        if times_vivos <= 1:
            break
        rodada+=1
    if rodada > rodada_max: rodada_max = rodada
    if rodada < rodada_min: rodada_min = rodada
    if texto:
        print(f'{time_vencedor} venceram a batalha\n')
        personagens = sorted(personagens, key=lambda d: d['time'])
        print(f'Eliminacoes: ')
        for personagem in personagens:
            print(personagem['nome']+': '+str(personagem['eliminacoes'])+' kills')

#RESULTADO NUMÉRICO
if cont_rodadas: 
    print(f'\nMínimo de rodadas: {rodada_min}')
    print(f'Máximo de rodadas: {rodada_max}')
print(f'\nDe {casos_teste} partida(s):')
personagens = sorted(personagens, key=lambda d: d['time'])
time = ''
for personagem in personagens:
    if personagem['time'] != time:
        time = personagem['time']
        print(personagem['time']+': '+str(personagem['vitorias']*100/casos_teste)+'%')