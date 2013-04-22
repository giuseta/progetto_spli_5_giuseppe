# coding: utf-8 -*-
# Questa funzione dato in ingresso il path di un file restituisci una stringa contenente il testo cifrato
# e crea un file di testo nel path col il testo cifrato

def encryption_function(txt_filename,key, min_chr, max_chr):
    import os
    #apertura del file e inserimento in una stringa
    input = open(txt_filename,'r')
    txt = input.read()
    

    #ciclo di rimpiazzamento per le lettere (le lettere maiuscole
    #corrispondenti vengono sostituite dallo stesso simbolo di quelle minuscole)
    
    txt=txt.lower()
    #range dei caratteri da sostituire
    #min_chr=int('21',16)
    #max_chr=int('fc',16)
    #limitiamo temporaneamente a solo l'alfabeto ascii

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
    directory = "./Cifrati/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    rest, output_filename = txt_filename.rsplit('/', 1)
    output_filename, rest = output_filename.rsplit('.', 1) 
    output_filename = directory + output_filename + "_crip.txt"
    out=open(output_filename, 'w')
    out.write(en_cri)
    out.close()
    
key = 3
min_chr = int("61",16)
max_chr = int("7a",16)
encryption_function('./Libri/MazzinieInternazionale.txt', key, min_chr, max_chr)
