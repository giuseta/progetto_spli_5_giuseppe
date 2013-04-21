# coding: utf-8 -*-
# Questa funzione dato in ingresso il path di un file restituisci una stringa contenente il testo cifrato
# e crea un file di testo nel path col il testo cifrato

def encryption_function(txtfilename,key):

    #apertura del file e inserimento in una stringa
    input = open(txtfilename,'r')
    txt = input.read()
    

    #ciclo di rimpiazzamento per le lettere (le lettere maiuscole
    #corrispondenti vengono sostituite dallo stesso simbolo di quelle minuscole)
    
    txt=txt.lower()
    #range dei caratteri da sostituire
    min_chr=int('21',16)
    max_chr=int('fc',16)
    num_chr=max_chr-min_chr+1 #numero di caratteri
    en_cri=''
    for let in txt:
        code=ord(let)
        if ((code>=min_chr) and (code<=max_chr)):
        	newcode=(code-min_chr+key)%num_chr
        	newcode+=min_chr
        	en_cri+=chr(newcode)
        else:
        	en_cri+=let        

    #creo il file di testo 
    out=open(txtfilename+'_crip', 'w')
    out.write(txt)
    out.close()
    
    
    #ritorno il testo cifrato
    
    return txt

#funziona!
