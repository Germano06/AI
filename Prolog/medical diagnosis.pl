go:- repeat,get_data,write('would you like to try again ( y/n)'),
	read(Reply), Reply = 'n'.

get_data:-write('Write the Patient name: '),nl,read(P),
	 hypothesis(P,D),!,write(P),write(' probably has the disease '),write(D),nl.

get_data:-write('Sorry we cant diagnose the disease'),nl.
	  /*write('would you like to continue'),read(Reply),Reply='y',!,repeat.*/

symptom(P,fever):-write('Does '),write(P),write(' have fever(y/n)?'),read(Reply),Reply='y'.

symptom(P,rash):-write('Does '),write(P),write(' have rash(y/n)?'),read(Reply),Reply='y'.

symptom(P,runny_nose):-write('Does  '),write(P),write(' have runnuing nose(y/n)?'),
	              read(Reply),Reply='y'.

symptom(P,cough):-write('Does '),write(P),write(' have cough(y/n)?'),read(Reply),Reply='y'.

symptom(P,chills):-write('Does '),write(P),write(' have chills(y/n)?'),read(Reply),Reply='y'.

symptom(P,sneezing):-write('Is  '),write(P),write(' sneezing  (y/n)?'),read(Reply),Reply='y'.

symptom(P,sore_throat):-write('Does '),write(P),write(' have soar_throat(y/n)?'),read(Reply),Reply='y'.

symptom(P,body_ache):-write('Does '),write(P),write(' have body ache(y/n)?'),read(Reply),Reply='y'.

symptom(P,headache):-write('Does '),write(P),write(' have headache(y/n)?'),read(Reply),Reply='y'.


hypothesis(P,measels):-symptom(P,fever),symptom(P,rash),symptom(P,cough).
hypothesis(P,flu):-symptom(P,fever),symptom(P,headache),symptom(P,cough),symptom(P,body_ache),symptom(P,runny_nose).
hypothesis(P,chicken_pox):-symptom(P,fever),symptom(P,rash),symptom(P,body_ache),symptom(P,chills).





