# coding: utf-8 -*-
# questa funzione prende in ingresso una lista di path di file di testo e restituisce in 
#uscita un dizionario con le frequenze dei soli caratteri
# se il testo è 'aaaaaacccckklllllllllll' restituisce il diz 'a': 6, 'c': 4, 'k': 2, 'l': 11,


def freq_distr(antologia):

    #creo un unica stringa contenente tutti i file di testo
    input=open(antologia,'r')
    txt=input.read()
    txt=txt.lower()  
    DizAscii={}    
    #ciclo che conta le occorrenze di ogni carattere ascii allinterno del testo
    for let in txt:
    	DizAscii[let]= DizAscii.get(let, 0)+1
		        	
    return DizAscii
        
#la funzione funziona bisogna scegliere se catalogare tutti i caratterri o solo le lettere dell'alfabeto	

