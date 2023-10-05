class budget_cons:

    def __init__(self, tipo):
        self.tipo = tipo
        self.reparti = list()
        self.MP = list()
        self.vendite = 0
        self.mix = 0
        self.prezzoTot = 0
        self.costoUnitario = 0
        self.nOdp = 0
        
    def setCostoUnitario(self, cu):
        ctot = self.costoUnitario * self.nOdp + cu
        self.nOdp = self.nOdp + 1
        self.costoUnitario = ctot/self.nOdp
        
    def getMix(self):
        return self.mix
    
    def getQuantita(self):
        return self.vendite
    
    def getPrezzo(self):
        if(self.vendite != 0):
            return self.prezzoTot/self.vendite
        else:
             return 0
    
    def getPrezzoTot(self):
        return self.prezzoTot
        
    def setVendita(self, q, prezzo):
        self.prezzoTot = self.prezzoTot + prezzo
        self.vendite = self.vendite + q
        
    def setMix(self, qtot):
        self.mix = self.vendite/qtot
        
        
    def setReparto(self, reparti):

        for i in range(len(reparti)):

            condition1 = True

            for j in range(len(self.reparti)):

                if(reparti[i].area == self.reparti[j].area):

                    self.reparti[j].setQOutput(reparti[i].qOutput)

                    for i2 in range(len(reparti[i].risorse)):

                        condition2 = True

                        for j2 in range(len(self.reparti[j].risorse)):

                            if(reparti[i].risorse[i2].nome == self.reparti[j].risorse[j2].nome):

                                self.reparti[j].risorse[j2].tempo = self.reparti[j].risorse[j2].tempo + reparti[i].risorse[i2].tempo
                                condition2 = False

                        if(condition2):
                            self.reparti[j].risorse.append(reparti[i].risorse[i2])

                    condition1 = False

            if(condition1):
                self.reparti.append(reparti[i])

                                                           
    def setMP(self, MP):

        for i in range(len(MP)):
            condition = True
            for j in range(len(self.MP)):

                if(MP[i].codice == self.MP[j].codice):
                    self.MP[j].q = MP[i].q + self.MP[j].q
                    self.MP[j].costoTot = MP[i].costoTot + self.MP[j].costoTot
                    condition = False

            if(condition):
                self.MP.append(MP[i])

    def stampa(self):
        
        print(self.tipo)
        print("Vendita: " + str(self.vendite))
        
        flag = 0;
        
        for i in range(len(self.reparti)):
            if(self.reparti[i].area == 'CQ'):
                print("Quantita prodotta: " + str(self.reparti[i].qOutput))
                flag = 1
                
        if(flag == 0):
            print("NO CONTROLLO QUALITA'")
        
        print("Mix %: " + str(self.mix))
        print("Ricavo: " + str(self.prezzoTot))
        print("Materie prime")
        for i in range(len(self.MP)):
            self.MP[i].stampa()
        print("Risorse")
        for i in range(len(self.reparti)):
            self.reparti[i].stampa()              