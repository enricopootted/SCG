import classi.budget_cons

class Articolo:

    def __init__(self, artodp):
        self.codice = artodp.articolo

        self.budget = classi.budget_cons.budget_cons('BUDGET')
        self.consuntivo = classi.budget_cons.budget_cons('CONSUNTIVO')
        
        self.fatturatoDollaroBudget = 0
        self.fatturatoDollaroCons = 0
        self.fatturatoYenBudget = 0
        self.fatturatoYenCons = 0
        self.fatturatoEuro = 0

        if(artodp.tipo == 'BUDGET'):
            self.Budget(artodp)
        else:
            self.Consuntivo(artodp)
            
        self.prezzoValCons = 0
        
    def setFatturato(self, fdb, fdc, fyb, fyc, fe):
        self.fatturatoDollaroBudget = self.fatturatoDollaroBudget + fdb
        self.fatturatoDollaroCons = self.fatturatoDollaroCons + fdc
        self.fatturatoYenBudget = self.fatturatoYenBudget + fyb
        self.fatturatoYenCons = self.fatturatoYenCons + fyc
        self.fatturatoEuro = self.fatturatoEuro + fe

    def setPrezzoValCons(self, prezzoTot):
        self.prezzoValCons = self.prezzoValCons + prezzoTot
        
    def getPrezzoValCons(self):
        return self.prezzoValCons

    def stampa(self):

        print(self.codice)
        self.budget.stampa()
        print("............................................")
        self.consuntivo.stampa()
        print("Ricavo scostamento valuta: " + str(self.prezzoValCons))
        print("--------------------------------------------")
            

    def Budget(self, artodp):

        self.budget.setReparto(artodp.reparti)
        self.budget.setMP(artodp.MP)
        if(artodp.costoUnitario != -1):
            self.budget.setCostoUnitario(artodp.costoUnitario)

    def Consuntivo(self, artodp):

        self.consuntivo.setReparto(artodp.reparti)
        self.consuntivo.setMP(artodp.MP)
        if(artodp.costoUnitario != -1):
            self.consuntivo.setCostoUnitario(artodp.costoUnitario)
