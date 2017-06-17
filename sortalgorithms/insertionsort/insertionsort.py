#!/usr/bin/env python3

def sortiranje(lista):
	tmp = 0
	for i in range(0, len(lista)-1):
		if lista[i] > lista[i+1]:
			tmp = lista[i+1]
			j = i + 1
			while j > 0 and lista[j-1] > tmp:
				lista[j] = lista[j-1]
				j = j-1
			lista[j] = tmp

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