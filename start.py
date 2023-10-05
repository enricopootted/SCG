import load.load as load
import load.AnalisiScostamenti as AS
import load.ScostamentoProdotto as SP

temp = load.Caricamento('files/Consumi.xlsx', 'files/Impiego orario risorse.xlsx', 'files/Costo orario risorse - budget.xlsx', 'files/Costo orario risorse - consuntivo.xlsx', 'files/Vendite.xlsx', 'files/Tassi di cambio.xlsx', 'files/Clienti.xlsx')

art = temp.caricamento()
 
totVenduto = 0
 
for i in range(len(art)):
    totVenduto = totVenduto + art[i].consuntivo.vendite
    
print("ELABORATO SCG DI FRANCESCO CORRINI ED ENRICO PERANI")
print("Si consiglia la visione dei dati dalla presentazione ppt poiche le stampe di python non sono ben tabulate")
print("Le stampe sono state fatte per prendere i dati da copiare nella presentazione")
print()
print()
print("Analisi degli scostamenti sull'aggregato di fatturato, costo e MON")
print()
analisiScostamenti = AS.AnalisiScostamenti(art, totVenduto)
analisiScostamenti.stampa()
 
scostamenti = list()
 
for i in range(len(art)):
    articolo = SP.ScostamentoProdotto(art[i], temp, totVenduto)
    scostamenti.append(articolo)
    
FDB = 0
FDC = 0
FYB = 0
FYC = 0
FE = 0
    
for i in range(len(art)):
    
    FDB = FDB + art[i].fatturatoDollaroBudget
    FDC = FDC + art[i].fatturatoDollaroCons
    
    FYB = FYB + art[i].fatturatoYenBudget
    FYC = FYC + art[i].fatturatoYenCons
    
    FE = FE + art[i].fatturatoEuro

print()
print()
print("Analisi scostamento di valuta")
print("L'obiettivo e' valutare quanto scostamento dipenda da un cambio valutario ma anche la divisione totale del fatturato")
print()
print("Fatturato\t" + str(FDB + FYB + FE) + "\tScostamento$\t" + str(FDB - FDC + FYB - FYC) + "\tFatturato Reale\t\t" + str(FDC + FYC + FE))
print("Fatturato$\t" + str(FDB) + "\tScostamento$\t" + str(FDB - FDC) + "\tFatturato Reale$\t" + str(FDC))
print("FatturatoY\t" + str(FYB) + "\tScostamentoY\t" + str(FYB - FYC) + "\tFatturato RealeY\t" + str(FYC))
print("FatturatoE\t" + str(FE) + "\t\t\tScostamentoE\t" + str(0) + "\t\t\tFatturato RealeE\t" + str(FE))

print()
print()

totBudget = 0
for i in range(len(art)):
    totBudget = totBudget + art[i].budget.vendite

condition = True

while(condition):
    condition = False
    
    for i in range(len(scostamenti) - 1):
        
        if(scostamenti[i].getScostamentoMONVolume() < scostamenti[i+1].getScostamentoMONVolume()):
            appoggio = scostamenti[i]
            scostamenti[i] = scostamenti[i+1]
            scostamenti[i+1] = appoggio
            condition = True
            
negativi = 0
positivi = 0
nonVenduti = 0

for i in range(len(scostamenti)):
    if(scostamenti[i].getScostamentoMONVolume() > 0):
        negativi = negativi + 1
        
    elif(scostamenti[i].getScostamentoMONVolume() < 0):
        positivi = positivi + 1
    else:
        nonVenduti = nonVenduti + 1
        
print("Analisi dello scostamento di volume")
print("Obiettivo: analizzare quali articoli hanno inciso maggiormente (in positivo ed in negativo) allo scostamento di volume")
print()

print("Volume di vendita a budget: " + str(totBudget))
print("Volume di vendita a consuntivo: " + str(analisiScostamenti.totVenduto))

print("Articolo\t\t\tDeltaV\t\t\tScostamentoMON\t\t\t\tPrezzoVendita\t\t\t\tCostoProduzione")

for i in range(5):
    print(scostamenti[i].articolo[0].codice + "\t\t\t" + str(int(scostamenti[i].articolo[0].budget.getMix()*analisiScostamenti.totVenduto - scostamenti[i].articolo[0].budget.vendite)) + "\t\t\t" + str(scostamenti[i].getScostamentoMONVolume()) + "\t\t\t" + str(scostamenti[i].articolo[0].budget.getPrezzo()) + "\t\t\t" + str(scostamenti[i].articolo[0].budget.costoUnitario))
    
print("------------")

for i in range(5):
    print(scostamenti[len(scostamenti) - 1 -i].articolo[0].codice + "\t\t\t" +  str(int(scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.getMix()*analisiScostamenti.totVenduto - scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.vendite)) + "\t\t\t" + str(scostamenti[len(scostamenti) - 1 -i].getScostamentoMONVolume()) + "\t\t\t" + str(scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.getPrezzo()) + "\t\t\t" + str(scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.costoUnitario))

print()
print("Articoli con scostamento di volume favorevole: " + str(positivi))
print("Articoli con scostamento di volume sfavorevole: " + str(negativi))
print("Articoli senza scostamento: " + str(nonVenduti))

condition = True

while(condition):
    condition = False
    
    for i in range(len(scostamenti) - 1):
        
        if(scostamenti[i].getScostamentoMONMix() < scostamenti[i+1].getScostamentoMONMix()):
            appoggio = scostamenti[i]
            scostamenti[i] = scostamenti[i+1]
            scostamenti[i+1] = appoggio
            condition = True

print()

print("Analisi dello scostamento di mix")
print("Obiettivo: analizzare quali articoli hanno inciso maggiormente (in positivo ed in negativo) allo scostamento di mix")
print()

print("Articolo\t\t\tScostamento Mix\t\t\tDeltaV\t\t\tPrezzo\t\t\tCosto")
for i in range(5):
    print(scostamenti[i].articolo[0].codice + "\t\t\t" + str(scostamenti[i].getScostamentoMONMix()) + "\t\t" + str(int(scostamenti[i].articolo[0].consuntivo.vendite - analisiScostamenti.totVenduto*scostamenti[i].articolo[0].budget.getMix())) + "\t\t" + str(scostamenti[i].articolo[0].budget.getPrezzo()) + "\t\t" + str(scostamenti[i].articolo[0].budget.costoUnitario))

print("------")
for i in range(5):
    print(scostamenti[len(scostamenti) - 1 -i].articolo[0].codice + "\t\t\t" + str(scostamenti[len(scostamenti) - 1 -i].getScostamentoMONMix()) + "\t\t" + str(int(scostamenti[len(scostamenti) - 1 -i].articolo[0].consuntivo.vendite - analisiScostamenti.totVenduto*scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.getMix())) + "\t\t" + str(scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.getPrezzo()) + "\t\t" + str(scostamenti[len(scostamenti) - 1 -i].articolo[0].budget.costoUnitario))


negativi = 0
positivi = 0
nonVenduti = 0

for i in range(len(scostamenti)):
    if(scostamenti[i].getScostamentoMONMix() > 0):
        negativi = negativi + 1
        
    elif(scostamenti[i].getScostamentoMONMix() < 0):
        positivi = positivi + 1
    else:
        nonVenduti = nonVenduti + 1
        
print()
print("Articoli con scostamento di mix favorevole: " + str(positivi))
print("Articoli con scostamento di mix sfavorevole: " + str(negativi))
print("Articoli senza scostamento: " + str(nonVenduti))


condition = True

while(condition):
    condition = False
    
    for i in range(len(scostamenti) - 1):
        
        if(scostamenti[i].getScostamentoMONPrezzi() < scostamenti[i+1].getScostamentoMONPrezzi()):
            appoggio = scostamenti[i]
            scostamenti[i] = scostamenti[i+1]
            scostamenti[i+1] = appoggio
            condition = True
            
print("Analisi dello scostamento di prezzi")
print("Obiettivo: analizzare quali articoli hanno inciso maggiormente (in positivo ed in negativo) allo scostamento di prezzi")
print("In particolare confrontando prezzi e costi a budget/consuntivo")
print()


print()
print("Articolo\t\t\tScostamento Prezzi\t\t\tPrezzoBudget/Consuntivo\t\t\tCostoBudget/Consuntivo")
for i in range(5):
    print(scostamenti[i].articolo[0].codice + "\t\t\t" + str(scostamenti[i].getScostamentoMONPrezzi()) + "\t\t\t" + str(scostamenti[i].articolo[0].budget.getPrezzo())+"/" +str(scostamenti[i].articolo[0].consuntivo.getPrezzo()) + "\t\t\t" +str(scostamenti[i].articolo[0].budget.costoUnitario)+"/"+ str(scostamenti[i].articolo[0].consuntivo.costoUnitario))

print("------")
for i in range(5):
    print(scostamenti[len(scostamenti) -1 -i].articolo[0].codice + "\t\t\t" + str(scostamenti[len(scostamenti) -1 -i].getScostamentoMONPrezzi()) + "\t\t\t" + str(scostamenti[len(scostamenti) -1 -i].articolo[0].budget.getPrezzo()) + "/"+ str(scostamenti[len(scostamenti) -1 -i].articolo[0].consuntivo.getPrezzo()) + "\t\t\t" + str(scostamenti[len(scostamenti) -1 -i].articolo[0].budget.costoUnitario) + "/" +  str(scostamenti[len(scostamenti) -1 -i].articolo[0].consuntivo.costoUnitario))

negativi = 0
positivi = 0
nonVenduti = 0

for i in range(len(scostamenti)):
    if(scostamenti[i].getScostamentoMONPrezzi() > 0):
        negativi = negativi + 1
        
    elif(scostamenti[i].getScostamentoMONPrezzi() < 0):
        positivi = positivi + 1
    else:
        nonVenduti = nonVenduti + 1
        
print()
print("Articoli con scostamento di prezzo favorevole: " + str(positivi))
print("Articoli con scostamento di prezzo sfavorevole: " + str(negativi))
print("Articoli senza scostamento: " + str(nonVenduti))

            

        
    