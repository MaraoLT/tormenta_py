from .basicas import *
from .objetos_classes import *


poderes_arcanista = {
    'Arcano de Batalha': '',
    'Aumento de Atributo': '',
    'Caldeirão do Bruxo': 'Bruxo, treinado em Ofício (alquimista)',
    'Conhecimento Mágico': '',
    'Contramágica Aprimorada': 'Dissipar Magia',
    'Envolto em Mistério': '',
    'Escriba Arcano': 'Mago, treinado em Ofício (escriba)',
    'Especialista em Escola': 'Bruxo, Mago',
    'Familiar': '',
    'Fluxo de Mana': 'nível 10',
    'Foco Vital': 'Bruxo',
    'Fortalecimento Arcano': 'nível 5',
    'Herança Aprimorada': 'Feiticeiro, nível 6',
    'Herança Superior': 'Herança Aprimorada, nível 11',
    'Magia Pungente': '',
    'Mestre em Escola': 'Especialista em Escola com a escola escolhida, nível 8',
    'Poder Mágico': '',
    # falta ainda
}

def verifica_poderes(personagem):
    


# Arcanista
def arcanista(personagem):
    '''
    
    '''
    funcoes_arcanista = {'caminho do arcanista': caminho_do_arcanista,
                        'magias': magias,
                        'poder de arcanista': poder_de_arcanista,
                        'alta arcana': alta_arcana}


    for i in range(personagem.nivel):
        for habilidade in personagem.classe.habilidades:
            nome_habilidade = formatacao(habilidade)
            if nome_habilidade in funcoes_arcanista:
                funcao_executada = funcoes_arcanista[nome_habilidade]
                funcao_executada(personagem)
            else:
                print(f'A função {nome_habilidade} não existe :(')

    def caminho_do_arcanista(personagem):
        print('A magia é um poder incrível, capaz de alterar a realidade. Esse poder tem fontes distintas e cada uma opera conforme suas próprias regras. Escolha uma das opções a seguir. Uma vez feita, essa escolha não pode ser mudada.')
        caminhos_arcanista = {
            'Bruxo': 'Bruxo. Você lança magias através de um foco — uma varinha, cajado, chapéu... Para lançar uma magia, você precisa empunhar o foco com uma mão (e gesticular com a outra) ou fazer um teste de Misticismo (CD 20 + o custo em PM da magia; se falhar, a magia não funciona, mas você gasta os PM mesmo assim). O foco tem RD 10 e PV iguais à metade dos seus, independentemente de seu material ou forma. Se for danificado, é totalmente restaurado na próxima vez que você recuperar seus PM. Se for destruído (reduzido a 0 PV), você fica atordoado por uma rodada. Você pode recuperar um foco destruído ou perdido com uma semana de trabalho e T$ 100. Seu atributo-chave para magias é Inteligência.',
            'Feiticeiro': 'Feiticeiro. Você lança magias através de um poder inato que corre em seu sangue. Escolha uma linhagem como origem de seus poderes (veja a página 39). Você recebe a herança básica da linhagem escolhida. Você não depende de nenhum item ou estudo, mas sua capacidade de aprender magias é limitada — você aprende uma magia nova a cada nível ímpar (3o, 5o, 7o etc.), em vez de a cada nível. Seu atributo-chave para magias é Carisma.', 
            'Mago': 'Mago. Você lança magias através de estudo e memorização de fórmulas arcanas. Você só pode lançar magias memorizadas; suas outras magias não podem ser lançadas, mesmo que você tenha pontos de mana para tal. Para memorizar magias, você precisa estudar seu grimório por uma hora. Quando faz isso, escolhe metade das magias que conhece (por exemplo, se conhece 7 magias, escolhe 3). Essas serão suas magias memorizadas. Você pode memorizar magias uma vez por dia. Caso não possa estudar (por não ter tempo, por ter perdido o grimório...), não poderá trocar suas magias memorizadas. Um grimório tem as mesmas estatísticas de um foco (veja acima) e pode ser recuperado da mesma forma. Você começa com uma magia adicional (para um total de 4) e, sempre que ganha acesso a um novo círculo de magias, aprende uma magia adicional daquele círculo. Seu atributo-chave para magias é Inteligência.'
                            }
        caminho_escolhido = escolhe_categoria(Palavra('caminho', 'caminhos'), caminhos_arcanista.keys(), 1, escolhidos_antes=[], genero=1)[0]
        personagem.caracteristicas.append(Habilidade(caminho_escolhido, caminhos_arcanista[caminho_escolhido][len({caminho_escolhido}+2):]))


    def magias(personagem):
        ...



    def poder_de_arcanista(personagem):
        poderes_possiveis = verifica_poderes(personagem)



    def alta_arcana(personagem):
        personagem.caracteristicas.append(Habilidade(nome='Alta Arcana', descricao='No nível 20, seu domínio das artes arcanas é total. O custo em PM de suas magias arcanas é reduzido à metade (após aplicar aprimoramentos e quaisquer outros efeitos que reduzam custo).'))