# coding: utf-8 -*-
#questa funzione confronta la distribuzione usata con l'attacco con quella reale della coppia in chiaro
#restituisce la percentuale di lettere corrette sostituite
def confr_function(listadecifrato,listachiaro):

	if (len(listachiaro)>len(listadecifrato)):
		k=len(listadecifrato)-1
	else:
		k=len(listachiaro)-1
	
	i=0
	for j in range(k):
		if (listachiaro[j]==listadecifrato[j]):
			i=i+1
			print('\nCarattere -'+listachiaro[j]+'- sostituito in maniera corretta')

		else:
			print('\nIl carattere -'+listachiaro[j]+'- è stato sostituito dal carattere -'+listadecifrato[j]+'-')

	perc=100*(i/float(k))
	
	print(i)
	
	print(perc)

	return perc

def confront_2(original_file, decrypted_file, min_chr, max_chr):
    o_file = open(original_file, 'r')
    d_file = open(decrypted_file, 'r')
    tot_count = 0 # total count of letters
    mis_count = 0 # total count of mismatched letters
    for o_line in o_file:
        d_line = d_file.readline()
        if not d_line: break #devo generare un errore
        index = 0 # index of the letter in d_line
        for o_let in o_line:
            code=ord(o_let)
            if ((code>=min_chr) and (code<=max_chr)):
                tot_count += 1
                if o_let!=d_line[index]: mis_count+=1
            index+=1

    perc = 100*(mis_count/float(tot_count)) # percentage of mismatched letters
    print("Percentuale lettere sbagliate: "+repr(perc))
    return perc





