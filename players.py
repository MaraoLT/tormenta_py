from dataclasses import dataclass


@dataclass
class Personagem:
        nome: str
        jogador: str
        nivel: int
        raca: str
        classe: Classe()
        # self.classe = self.Classe()
        origem: str
        divindade: str
        # self.atributos = self.Atributos()
        PV_MAX: int
        PV: int
        PM_MAX: int
        PM: int
        defesa: int
        # self.pericias = self.Pericias()


    def imprime():
        print('{self.nome} ({self.jogador})')
        print('{self.classe}/{self.raca} {self.nivel}')



# talvez seja melhor usar dicionario
class Atributos:
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma) -> None:
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma


# melhor usar como dicionario e fazer uma classe chamada 'pericia'
class Pericias:
    def __init__(self) -> None:
        self.acrobacia = acrobacia
        self.adestramento = adestramento
        self.atletismo = atletismo
        self.atuacao = atuacao
        self.cavalgar = cavalgar
        self.conhecimento = conhecimento
        self.cura = cura
        self.diplomacia = diplomacia
        self.enganacao = enganacao
        self.fortitude = fortitude
        self.furtividade = furtividade
        self.guerra = guerra
        self.iniciativa = iniciativa
        self.intimidacao = intimidacao
        self.intuicao = intuicao
        self.investigacao = investigacao
        self.jogatina = jogatina



class Classe:
    def __init__(self,):
        self.arcanista = arcanista
        self.barbaro = barbaro
        self.bardo = bardo
        self.bucaneiro = bucaneiro
        self.cacador = cacador
        self.cavaleiro = cavaleiro
        self.clerigo = clerigo
        self.druida = druida
        self.guerreiro = guerreiro
        self.inventor = inventor
        self.ladino = ladino
        self. lutador = lutador
        self.nobre = nobre
        self.paladino = paladino


def main():
    gustavo = Personagem('Doende Mardito', 'Gustavo', 1, 'goblin', 'bucaneiro')
    gustavo.imprime()



main()