#coding:cp1252

import pandas as pd
import classi.Articolo as Articolo
import classi.ArticoloOdp
import classi.budget_cons as budget_cons
import classi.MateriaPrima as MateriaPrima
import classi.Reparto as Reparto
import classi.Risorsa as Risorsa

class Caricamento:
    def __init__(self, cons, ris, corb, corc, vend, val, clienti):

        self.Consumi = pd.read_excel(cons, index_col=0)  

        by = list()
        by.append('Nr articolo')
        by.append('Nr. documento')
        self.Consumi = self.Consumi.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

        self.Risorse = pd.read_excel(ris, index_col=3)  

        by2 = list()
        by2.append('nr articolo')
        by2.append('Nr. Ordine di produzione')
        by2.append('Nr. Area di produzione')
        self.Risorse = self.Risorse.sort_values(by2, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
        
        self.COR_Budget = pd.read_excel(corb, index_col=False)

        self.COR_Consuntivo = pd.read_excel(corc, index_col=False)
        
        self.Vendite = pd.read_excel(vend);

        self.Valuta = pd.read_excel(val);

        self.Clienti = pd.read_excel(clienti);
        self.valute = list()

    def caricamento(self):

        artodp = list()
        self.caricaConsumi(artodp)
        self.caricaRisorse(artodp)
        
        for i in range(len(artodp)):
            artodp[i].getCostoUnitario()
        
        art = list()

        for i in range(len(artodp)):

            Condition = True

            for j in range(len(art)):

                if(artodp[i].articolo == art[j].codice):

                    if(artodp[i].tipo == 'BUDGET'):
                        art[j].Budget(artodp[i])
                    else:
                        art[j].Consuntivo(artodp[i])

                    Condition = False

            if(Condition):
                art.append(Articolo.Articolo(artodp[i]))
                
   
        self.caricaValute()
        self.caricaVendite(art)

        return art

    def caricaConsumi(self, artodp):

        c = -1

        lastArt = None
        lastOdp = None
        
        
        for i in range(len(self.Consumi)):
            
            if(lastArt != self.Consumi['Nr articolo'].iloc[i] or lastOdp != self.Consumi['Nr. documento'].iloc[i]):
                
                lastArt = self.Consumi['Nr articolo'].iloc[i]
                lastOdp = self.Consumi['Nr. documento'].iloc[i]
                artodp.append(classi.ArticoloOdp.ArticoloOdp(self.Consumi['Nr articolo'].iloc[i], self.Consumi['Nr. documento'].iloc[i], self.Consumi['Budget/cons'].iloc[i], self.Consumi['Codice MP'].iloc[i], self.Consumi['Quantità MP impiegata'].iloc[i], self.Consumi['Importo costo (TOTALE)'].iloc[i]))
                c = c + 1
                
                              
            else:

                artodp[c].setMP(self.Consumi['Codice MP'].iloc[i], self.Consumi['Quantità MP impiegata'].iloc[i], self.Consumi['Importo costo (TOTALE)'].iloc[i])
                
    def caricaRisorse(self, artodp):

        c = -1

        lastArt = None
        lastOdp = None
        lastReparto = None
        rep = None

        for i in range(len(self.Risorse)):

            costo = 0

            if (self.Risorse['budget/consuntivo'].iloc[i] == 'BUDGET'):
                costo = self.COR_Budget['Costo orario (€/h)'].loc[(self.COR_Budget['Risorsa'] == self.Risorse['Risorsa'].iloc[i]) & (self.COR_Budget['Area di produzione'] == self.Risorse['Nr. Area di produzione'].iloc[i])]
            else:
                costo = self.COR_Consuntivo['Costo orario (€/h)'].loc[(self.COR_Consuntivo['Risorsa'] == self.Risorse['Risorsa'].iloc[i]) & (self.COR_Consuntivo['Area di produzione'] == self.Risorse['Nr. Area di produzione'].iloc[i])]

            costo = costo.values[0]
            if(lastArt != self.Risorse['nr articolo'].iloc[i] or lastOdp != self.Risorse['Nr. Ordine di produzione'].iloc[i]):
                c = c + 1
                rep = Reparto.Reparto(self.Risorse['Nr. Area di produzione'].iloc[i], self.Risorse['Risorsa'].iloc[i], self.Risorse['Tempo risorsa'].iloc[i], self.Risorse['Quantità di output'].iloc[i], costo)
                artodp[c].setReparto(rep)
                lastArt = self.Risorse['nr articolo'].iloc[i]
                lastOdp = self.Risorse['Nr. Ordine di produzione'].iloc[i]
                lastReparto = self.Risorse['Nr. Area di produzione'].iloc[i]
            elif(lastReparto != self.Risorse['Nr. Area di produzione'].iloc[i]):
                rep = Reparto.Reparto(self.Risorse['Nr. Area di produzione'].iloc[i], self.Risorse['Risorsa'].iloc[i], self.Risorse['Tempo risorsa'].iloc[i], self.Risorse['Quantità di output'].iloc[i], costo)
                artodp[c].setReparto(rep)
                lastArt = self.Risorse['nr articolo'].iloc[i]
                lastOdp = self.Risorse['Nr. Ordine di produzione'].iloc[i]
                lastReparto = self.Risorse['Nr. Area di produzione'].iloc[i]
            else:
                artodp[c].reparti[len(artodp[c].reparti) - 1].setRisorsa(self.Risorse['Risorsa'].iloc[i], self.Risorse['Tempo risorsa'].iloc[i], costo)
                artodp[c].reparti[len(artodp[c].reparti) - 1].setQOutput(self.Risorse['Quantità di output'].iloc[i])
                lastArt = self.Risorse['nr articolo'].iloc[i]
                lastOdp = self.Risorse['Nr. Ordine di produzione'].iloc[i]
                lastReparto = self.Risorse['Nr. Area di produzione'].iloc[i]
                
    def caricaValute(self):
        #for i in range(len(self.Valuta)):
            #self.valute.append(self.Valuta['Tasso di cambio medio'].iloc[i])
            
        self.valute.append(1)
        self.valute.append(1.0541)
        self.valute.append(123)
        self.valute.append(1)
        self.valute.append(1.1993)
        self.valute.append(135.01)
        

    def caricaVendite(self, art):
        totBudget = 0
        totCons = 0
        for i in range(len(self.Vendite)):
            for j in range(len(art)):
                if(art[j].codice == self.Vendite['Nr articolo'].iloc[i]):
                    codiceValuta = self.Clienti['Valuta'].loc[self.Clienti['Nr.'] == self.Vendite['Nr. origine'].iloc[i]]
                    if(self.Vendite['budget/cons'].iloc[i] == 'BUDGET'):
                        prezzo = 0
                        if(int(codiceValuta) == 1):
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]
                        elif (int(codiceValuta) == 2):
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[1]
                        else:
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[2]
                    
                        art[j].budget.setVendita(self.Vendite['Quantità'].iloc[i], prezzo)
                        totBudget = totBudget + self.Vendite['Quantità'].iloc[i]
                
                    else:
                        prezzo = 0
                        prezzoCons = 0
                        fatturatoEuro = 0
                        fatturatoDollaroBudget = 0
                        fatturatoYenBudget = 0
                        fatturatoDollaroConsuntivo = 0
                        fatturatoYenConsuntivo = 0

                        if(int(codiceValuta) == 1):
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]
                            prezzoCons = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]
                            fatturatoEuro = fatturatoEuro + prezzo
                        elif (int(codiceValuta) == 2):
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[1]
                            prezzoCons = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[4]
                            fatturatoDollaroBudget = fatturatoDollaroBudget + prezzo
                            fatturatoDollaroConsuntivo = fatturatoDollaroConsuntivo + prezzoCons
                        else:
                            prezzo = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[2]
                            prezzoCons = self.Vendite['Importo vendita in valuta locale (TOTALE VENDITA)'].iloc[i]/self.valute[5]
                            fatturatoYenBudget = fatturatoYenBudget + prezzo
                            fatturatoYenConsuntivo = fatturatoYenConsuntivo + prezzoCons

                        art[j].consuntivo.setVendita(self.Vendite['Quantità'].iloc[i], prezzo)
                        art[j].setPrezzoValCons(prezzoCons)
                        totCons = totCons + self.Vendite['Quantità'].iloc[i]
                        art[j].setFatturato(fatturatoDollaroBudget, fatturatoDollaroConsuntivo, fatturatoYenBudget, fatturatoYenConsuntivo, fatturatoEuro)
                    break
            
        for i in range(len(art)):
            art[i].budget.setMix(totBudget)
            art[i].consuntivo.setMix(totCons)


        
                    
                

                

                

