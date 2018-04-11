#!/usr/bin/env python3
lew={"imie":"Leon", "cecha": "odwazny", "typ": "lew"}
delfin={"imie":"Dodo", "cecha": "zabawny", "typ": "delfin"}
osiol={"imie":"Muniek", "cecha": "uparty", "typ": "osiol"}
lis={"imie":"Chytrusek", "cecha": "chytry", "typ": "lis"}
kot={"imie":"Kot w butach", "cecha": "buty", "typ": "kot"}
lista= [ lew, delfin, osiol, lis, kot]



print ("CALA STRUKTURA")
for animal in lista:
	#print animal.title()#jak wyswietlac nazwe slownika
	for attribute in animal:
		print (attribute+ ": "+animal[attribute] + "\n")
	
		
		
print ("\n DRUGIE ZWIERZE")
for attribute in lista[1]:
	print (attribute+ ": "+lista[1][attribute])
	
	
	
print ("\n \n IMIONA WSZYSTKICH ZWIERZAT \n")
for animal in lista:
	print(animal["imie"] )
		

	
	
	



		
