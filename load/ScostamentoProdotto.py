import load.AnalisiScostamenti as AS

class ScostamentoProdotto:
    def __init__(self, art, ld, totVenduto):
        
        self.articolo = list()
        self.articolo.append(art)
        
        self.scostamenti = AS.AnalisiScostamenti(self.articolo, totVenduto)
        
        self.ld = ld
        
    
    def getScostamentoMONVolume(self):
        return self.scostamenti.scostamentoVolume - self.scostamenti.scostamentoCostoVolume
    
    def getScostamentoMONMix(self):
        return self.scostamenti.scostamentoMix - self.scostamenti.scostamentoCostoMix
    
    def getScostamentoMONPrezzi(self):
        return self.scostamenti.scostamentoPrezzi - self.scostamenti.scostamentoCostoPrezzi
        
                
        