# coding: utf-8 -*-
#questa funzione prende in ingresso due liste di lettere che rappresentano le frequenze di riferimento,
# 
# e restituisce una stringa contenente il testo decifrato e produce un file col testo decifrato
from freq_distr import *
from ordDiz import *
from confr_function import *

def decryption_function(txt_cifrato,path_antologia, min_chr, max_chr):
    import os 
    #apertura del file e inserimento del testo cifrato in  una stringa
    input = open(txt_cifrato,'r')
    txt = input.read()
    input.close()
    txt=txt.lower()
    
    #creo la lista delle frequenze dei simboli del testo cifrato in ordine crescente
    freq_cifrato = ordDiz(freq_distr(txt_cifrato, min_chr, max_chr))
    #creo la lista delle frequenze dei simboli dell'antologia
    freq_antologia= ordDiz(freq_distr(path_antologia, min_chr, max_chr)) 
    decri_text=''
    
    for let in txt:        
        code=ord(let)
        if ((code>=min_chr) and (code<=max_chr)):
            posizione_cifrato=freq_cifrato.index(let)
            newlet=freq_antologia[posizione_cifrato]
            decri_text+=newlet
        else:
            decri_text+=let
    
    
    #creazione del file di testo  
    directory = "./Decifrati/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    rest, output_filename = txt_cifrato.rsplit('/', 1)
    output_filename, rest = output_filename.rsplit('.', 1) 
    output_filename = directory + output_filename + "_decrip.txt"
    out=open(output_filename, 'w')
    out.write(decri_text)
    out.close()
    
    return output_filename
    
min_chr = int("61",16)
max_chr = int("7a",16)
decrypted_file = decryption_function('./Cifrati/MazzinieInternazionale_crip.txt','./Libri/Antologia_libri', min_chr, max_chr)
#freq_chiaro= ordDiz(freq_distr('/home/mattia/Dropbox/progetto_spli/prog_5/Libri/MazzinieInternazionale'))
#freq_antologia= ordDiz(freq_distr('/home/mattia/Dropbox/progetto_spli/prog_5/Libri/Antologia_libri'))
#confr_function(freq_antologia,freq_chiaro)
original_file = './Libri/MazzinieInternazionale.txt'
confront_2(original_file, decrypted_file, min_chr, max_chr)
