#!/usr/bin/env python3

def sortiranje(lista):
	pmin = 0
	for i in range(0, len(lista)):
		for j in range(i + 1, len(lista)):
			if lista[pmin] > lista[j]:
				pmin = j

		tmp = lista[i]
		lista[i] = lista[pmin]
		lista[pmin] = tmp

afile = open("zasort.txt")
data = afile.readlines()

for line in data:
	words = line.split()

print(words)

afile.close()

lista = []

lista = list(map(int, words))

sortiranje(lista)
print(lista)

afile2 = open("sortirano.txt", "w" )
for i in range(0, len(lista)):
	afile2.write(str(lista[i]))
	afile2.write(' ')
afile.close()