# coding: utf-8 -*-
#funzione che dato un dizionario in ingresso restituisce una lista dei caratteri ordinati in maniera crescente
#secondo la loro distribuzione

def ordDiz(diz):
	    
    items=diz.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    list=[ backitems[i][1] for i in range(0,len(backitems))]
    list.reverse()
    return list

#la funzione funziona
