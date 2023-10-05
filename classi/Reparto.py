import classi.Risorsa

class Reparto:

    def __init__(self, area, nome, tempo, qOutput, costo):
        self.area = area
        self.risorse = list()
        self.setRisorsa(nome, tempo, costo)
        self.qOutput = 0
        self.setQOutput(qOutput)

    def setRisorsa(self, nome, tempo, costo):
        self.risorse.append(classi.Risorsa.Risorsa(nome, tempo, costo))

    def setQOutput(self, qOutput):
        self.qOutput = self.qOutput + qOutput

    def getCostoTot(self):
        costo = 0
        for i in range(len(self.risorse)):
            costo = costo + self.risorse[i].getCosto()

        return costo

    def stampa(self):
        print("Reparto: " + str(self.area) + ", output: " + str(self.qOutput))
        for i in range(len(self.risorse)):
            self.risorse[i].stampa()
        print("")