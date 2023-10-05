import classi.MateriaPrima
import classi.Reparto
import classi.Risorsa

class ArticoloOdp:

    def __init__(self, articolo, odp, tipo, codice, q, costo):
        self.articolo = articolo
        self.odp = odp
        self.tipo = tipo
        self.MP = list()
        self.setMP(codice, q, costo)
        self.reparti = list()
        self.costoUnitario = 0
        
    def getCostoUnitarioMP(self):
        
        stringa = "D"
        index = -1
        costoMP = 0
        
        for i in range(len(self.reparti)):
                
            if(self.reparti[i].area < stringa and self.reparti[i].qOutput != 0):
                stringa = self.reparti[i].area
                index = i
                
        if(index == -1):
            return -1
        for i in range(len(self.MP)):
            costoMP = costoMP + self.MP[i].getCostoTot()
            
        return costoMP/self.reparti[index].qOutput

        
    def getCostoUnitarioRisorse(self):
        
        c = 0
        produzione = 0
        costiFissi = 0
        
        for i in range(len(self.reparti)):
            produzione = produzione + self.reparti[i].qOutput
            if(self.reparti[i].qOutput == 0):
                costiFissi = costiFissi + self.reparti[i].getCostoTot()
                
        for i in range(len(self.reparti)):
            if(self.reparti[i].qOutput != 0):
                c = c + self.reparti[i].getCostoTot()/self.reparti[i].qOutput + costiFissi/produzione
                 
        return c
        
    def getCostoUnitario(self):
        
        costi = self.getCostoUnitarioRisorse()
        costoMP = self.getCostoUnitarioMP()
        
        self.costoUnitario = costi + costoMP
        
        if(costoMP == -1):
            self.costoUnitario = -1

    def getCodiceArticolo(self):
        return self.articolo

    def getCodiceODP(self):
        return self.odp

    def getTipo(self):
        return self.tipo

    def getMP(self):
        return self.MP

    def setMP(self, codice, q, costoTot):
        self.MP.append(classi.MateriaPrima.MateriaPrima(codice, q, costoTot))

    def setReparto(self, reparto):
        self.reparti.append(reparto)

    def stampa(self):

        print("------------------------------------------------------------")
        print(self.articolo + ", " + self.odp)
        print(self.tipo)
        print("Materie prime")
        for i in range(len(self.MP)):
            self.MP[i].stampa()
        print("Risorse")
        for i in range(len(self.reparti)):
            self.reparti[i].stampa()
        print("------------------------------------------------------------")