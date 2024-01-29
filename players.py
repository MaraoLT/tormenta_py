class Personagem:
    def __init__(self, PV_MAX, PV, PM_MAX, PM) -> None:
        self.nome = nome
        self.jogador = jogador
        self.nivel = nivel
        self.raca = raca
        self.classe = classe
        self.origem = origem
        self.divindade = divindade
        self.atributos = self.Atributos()
        self.PV_MAX = PV_MAX
        self.PV = PV
        self.PM_MAX = PM_MAX
        self.PM = PM
        self.defesa = defesa
        self.pericias = self.Pericias()



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