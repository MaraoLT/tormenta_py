#TESTE RPG 1x1
# Escrita de personagem:
# {'nome':'nome', 'PV': 0, 'defesa': 0, 'ataque': 0, 'forca': 0, 'agilidade': 0, 'dano': '0d0', 'time': 'time'}
###
#A fazer:
# -Criticos e Nulos V
# -Mais opções de ataques (mínimo 2)
###
from random import randint
import os
import ast

texto = False
casos_teste = 1
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
    margem_critico = 20 #para personalizar críticos futuramente
    d20 = rolagem('1d20')
    if d20 <= 1:
        golpe = 0
        if texto: print(atacante['nome']+' errou MUITO o golpe em '+defensor['nome'])
        return golpe;
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

#LEITURA DO ARQUIVO
path = "/Users/Ainaras/Programação/Programação/Minhas ideias/RPG"
with open(os.path.join(path, 'personagens_1x1.txt')) as arquivo:
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
#adicionando 'vitorias' aos personagens
for i in range(num_personagens):
    personagens[i]['vitorias'] = 0  
PVs = {}
for personagem in personagens:
    PVs[personagem['nome']] = personagem['PV']
rodada_max = 0
rodada_min = 100000
###BATALHA##
for j in range(casos_teste):
    rodada = 1
    for personagem in personagens:
        personagem['PV'] = PVs[personagem['nome']]
    personagens = iniciativa()
    if texto: 
        for personagem in personagens: print(personagem['nome']+' iniciativa: '+str(personagem['iniciativa']))
    while True:
        if texto: print(f'Rodada {rodada}:')
        for i in range(num_personagens):
            if i == 0: f = 1
            elif i == 1: f = 0
            personagens[f]['PV'] -= golpe(personagens[i], personagens[f])
            if personagens[f]['PV'] <= 0:
                personagens[f]['PV'] = 0
                vencedor = personagens[i]['nome']
                personagens[i]['vitorias']+=1
                break;
        if texto:
            for personagem in personagens: print(personagem['nome']+' PV: '+str(personagem['PV']))
            print('')
        if personagens[f]['PV'] <= 0:
            break;
        rodada+=1
    if rodada > rodada_max: rodada_max = rodada
    if rodada < rodada_min: rodada_min = rodada
    if texto: print(f'{vencedor} venceu a batalha\n')

#RESULTADO NUMÉRICO
if texto:
    print(f'Mínimo de rodadas: {rodada_min}')
    print(f'Máximo de rodadas: {rodada_max}')
    print(f'De {casos_teste}:')
personagens = sorted(personagens, key=lambda d: d['nome'])
for personagem in personagens:
    print(personagem['nome']+': '+str(personagem['vitorias']*100/casos_teste)+'%')