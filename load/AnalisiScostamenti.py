

class AnalisiScostamenti:
    
    def __init__(self, art, totVenduto):
        
        self.ricavoBudget = 0
        self.scostamentoVolume = 0
        self.scostamentoMix = 0
        self.scostamentoPrezzi = 0
        self.scostamentoValuta = 0
        
        self.totVenduto = totVenduto
        
        self.costoBudget = 0
        self.scostamentoCostoVolume = 0
        self.scostamentoCostoMix = 0
        self.scostamentoCostoPrezzi = 0
        
        self.calcolaRicavoBudget(art)
        self.calcolaScostamentoVolume(art)
        self.calcolaScostamentoMix(art)
        self.calcolaScostamentoPrezzi(art)
        self.calcolaScostamentoValuta(art)
                
    def calcolaRicavoBudget(self, art):
        
        for i in range(len(art)):
            self.ricavoBudget = self.ricavoBudget + art[i].budget.getPrezzoTot()
            self.costoBudget = self.costoBudget + art[i].budget.costoUnitario*art[i].budget.getQuantita()
            
    def calcolaScostamentoVolume(self, art):
        
        ricavo = 0
        costo = 0
                    
            
        for i in range(len(art)):
            ricavo = ricavo + art[i].budget.getPrezzo()*self.totVenduto*art[i].budget.getMix()
            costo = costo + art[i].budget.costoUnitario*self.totVenduto*art[i].budget.getMix()
                    
        self.scostamentoVolume = self.ricavoBudget - ricavo
        self.scostamentoCostoVolume = self.costoBudget - costo
            
    def calcolaScostamentoMix(self, art):
        
        ricavo = 0
        costo = 0
        
        for i in range(len(art)):
            ricavo = ricavo + art[i].budget.getPrezzo()*art[i].consuntivo.getQuantita()
            costo = costo + art[i].budget.costoUnitario*art[i].consuntivo.getQuantita()
            
        self.scostamentoMix = self.ricavoBudget - self.scostamentoVolume - ricavo
        self.scostamentoCostoMix = self.costoBudget - self.scostamentoCostoVolume - costo
        
    def calcolaScostamentoPrezzi(self, art):
        
        ricavo = 0
        costo = 0
        
        for i in range(len(art)):
            ricavo = ricavo + art[i].consuntivo.getPrezzoTot()
            costo = costo + art[i].consuntivo.costoUnitario*art[i].consuntivo.getQuantita()
            
        self.scostamentoPrezzi = self.ricavoBudget - self.scostamentoVolume - self.scostamentoMix - ricavo
        self.scostamentoCostoPrezzi = self.costoBudget - self.scostamentoCostoVolume - self.scostamentoCostoMix - costo
        
    def calcolaScostamentoValuta(self, art):
        
        ricavo = 0
        
        for i in range(len(art)):
            ricavo = ricavo + art[i].getPrezzoValCons()
            
        self.scostamentoValuta = self.ricavoBudget - self.scostamentoVolume - self.scostamentoMix - self.scostamentoPrezzi - ricavo
                
    def stampa(self):
        
        print("Row\t\t\tFatturato\t\t\t\tCosto\t\t\t\t\tMON" )
        
        print("BUDGET\t\t\t" + str(self.ricavoBudget) + "\t\t\t" + str(self.costoBudget) + "\t\t\t" + str(self.ricavoBudget - self.costoBudget))
        print("Scostamento\t\t" + str(self.scostamentoVolume) + "\t\t\t" + str(self.scostamentoCostoVolume) + "\t\t\t" + str(self.scostamentoVolume - self.scostamentoCostoVolume))
        nuovoFatturato = self.ricavoBudget - self.scostamentoVolume
        nuovoCosto = self.costoBudget - self.scostamentoCostoVolume
        nuovoMON = nuovoFatturato - nuovoCosto
        
        print("MIX_T\t\t\t" + str(nuovoFatturato) + "\t\t\t" + str(nuovoCosto) + "\t\t\t" + str(nuovoMON))
        print("Scostamento\t\t" + str(self.scostamentoMix) + "\t\t\t" + str(self.scostamentoCostoMix) + "\t\t\t" + str(self.scostamentoMix - self.scostamentoCostoMix))
        nuovoFatturato = nuovoFatturato - self.scostamentoMix
        nuovoCosto = nuovoCosto - self.scostamentoCostoMix
        nuovoMON = nuovoFatturato - nuovoCosto
        
        print("MIX_E\t\t\t" + str(nuovoFatturato) + "\t\t\t" + str(nuovoCosto) + "\t\t\t" + str(nuovoMON))
        print("Scostamento\t\t" + str(self.scostamentoPrezzi) + "\t\t\t" + str(self.scostamentoCostoPrezzi) + "\t\t\t" + str(self.scostamentoPrezzi - self.scostamentoCostoPrezzi))
        nuovoFatturato = nuovoFatturato - self.scostamentoPrezzi
        nuovoCosto = nuovoCosto - self.scostamentoCostoPrezzi
        nuovoMON = nuovoFatturato - nuovoCosto
        
        print("CONS\t\t\t" + str(nuovoFatturato) + "\t\t\t" + str(nuovoCosto) + "\t\t\t" + str(nuovoMON))
        print("Scostamento\t\t" + str(self.scostamentoValuta) + "\t\t\t0\t\t\t\t\t" + str(self.scostamentoValuta))
        nuovoFatturato = nuovoFatturato - self.scostamentoValuta
        nuovoMON = nuovoFatturato - nuovoCosto
        
        print("CONS_V\t\t\t" + str(nuovoFatturato) + "\t\t\t" + str(nuovoCosto) + "\t\t\t" + str(nuovoMON))

        
        




            
            
        
            
        
        
    