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



		
