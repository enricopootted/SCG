class Risorsa:

    def __init__(self, nome, tempo, costo):
        self.nome = nome
        self.tempo = tempo
        self.costo = costo

    def getCosto(self):
        return self.tempo*self.costo

    def stampa(self):
        print("Risorsa: " + str(self.nome) + ", tempo: " + str(self.tempo) + ", costo: " + str(self.costo))
