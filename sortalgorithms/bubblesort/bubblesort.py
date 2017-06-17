#!/usr/bin/env python3

def sortiranje(lista):
	tmp = 0
	for i in range(len(lista)-1, 0, -1):
		for j in range(i):
			if lista[j] > lista[j+1]:
				tmp = lista[j]
				lista[j] = lista[j+1]
				lista[j+1] = tmp

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