# coding: utf-8 -*-
#questa funzione prende in ingresso due liste di lettere che rappresentano le frequenze di riferimento,
# 
# e restituisce una stringa contenente il testo decifrato e produce un file col testo decifrato
from freq_distr import *
from ordDiz import *
from confr_function import *

def decryption_function(pathcifrato,pathantologia):
    
    #apertura del file e inserimento del testo cifrato in  una stringa
    input = open(pathcifrato,'r')
    txt = input.read()
    input.close()
    txt=txt.lower()
    
    #creo la lista delle frequenze dei simboli del testo cifrato in ordine crescente
    freq_cifrato = ordDiz(freq_distr(pathcifrato))
    #creo la lista delle frequenze dei simboli dell'antologia
    freq_antologia= ordDiz(freq_distr(pathantologia)) 
    decri_text=''
    
    for let in txt:
    	posizionecifrato=freq_cifrato.index(let)
    	newlet=freq_antologia[posizionecifrato]
    	decri_text+=newlet
    
    
    #ciclo di decifratura
#    j=0
#
#    for i in list:
#        txt=txt.replace(i,frequenze[j])
#        j=j+1
        
    #creazione del file di testo 
    
    out=open(pathcifrato+'_decrip', 'w')
    out.write(decri_text)
    out.close()
    
decryption_function('/home/mattia/Scrivania/pip','/home/mattia/Dropbox/progetto_spli/prog_5/Libri/Antologia_libri')
freq_chiaro= ordDiz(freq_distr('/home/mattia/Dropbox/progetto_spli/prog_5/Libri/MazzinieInternazionale'))
freq_antologia= ordDiz(freq_distr('/home/mattia/Dropbox/progetto_spli/prog_5/Libri/Antologia_libri'))
confr_function(freq_antologia,freq_chiaro)

