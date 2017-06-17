#!/usr/bin/env python3

def sortiranje(lista):
	razmak = len(lista) // 3
	while razmak > 0:
		for pocetak in range(razmak):
				modinsertsort(lista, pocetak, razmak) 
		razmak = razmak // 3

def modinsertsort(lista, poc, raz):
	for i in range(poc+raz, len(lista), raz):
		tmp = lista[i]
		j = i
		while j >= raz and lista[j-raz] > tmp:
			lista[j] = lista[j-raz]
			j = j-raz
		lista[j] = tmp

afile = open("zasort.txt")
data = afile.readlines()

for line in data:
	words = line.split()

afile.close()

lista = []

lista = list(map(int, words))

print(lista)
sortiranje(lista)
print(lista)

afile2 = open("sortirano.txt", "w" )
for i in range(0, len(lista)):
	afile2.write(str(lista[i]))
	afile2.write(' ')
afile.close()