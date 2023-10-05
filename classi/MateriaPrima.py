class MateriaPrima:

    def __init__(self, codice, q, costoTot):
        self.codice = codice
        self.q = q
        self.costoTot = costoTot

    def getCodiceMP(self):
        return self.codice

    def getQuantita(self):
        return self.q

    def getCostoTot(self):
        return self.costoTot

    def getCostoUnitario(self):
        return self.costoTot/self.q

    def stampa(self):
        print("MP: " + str(self.codice) + ", quantita: " + str(self.q) + ", costoTot: " + str(self.costoTot))
