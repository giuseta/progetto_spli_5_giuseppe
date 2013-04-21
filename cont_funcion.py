#questa funzione di attacco deve contare il numero di caratteti escludendo gli spazi e i new line e restituisce
#una lista con i caratteri ordinati, (serve per il cifrato)
import ordDiz

def cont_distr(pathcifrato):

    #apertura del file e inserimento in una stringa
    input = open(pathcifrato,'r')
    txt = input.read()
    
    DizAscii={}    
    #ciclo che conta le occorrenze di ogni carattere ascii allinterno del testo
    for let in txt:
	DizAscii[let]= DizAscii.get(let, 0) + 1
        	

    #soluzione con lo scotch..forse funziona senza questi accorgimenti
#    del DizAscii['\n']
#    del DizAscii['.']
#    del DizAscii[',']
#    del DizAscii[':']
#    del DizAscii[',']
#    del DizAscii[' ']

    list=ordDiz(DizAscii)
# prendiamo solo le prime 26 occorrenze che dovrebbero corrispondere ai caratteri (forse dobbiamo escludere la punteggiaturea!!)
# in questo modo però applichiamo una conoscenza che non dovremmo avere, cioè che non abbiamo sostituito la punteggiature gli spazi etc
    return list


