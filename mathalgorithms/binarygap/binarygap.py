#!/usr/bin/env python3


afile = open("binary.txt")
data = afile.readlines()
broj = str(data)
print(broj)
broj = broj[2:len(broj)-2]
afile.close()
print(broj)

duz = len(broj) - 1
marker = 0
tmp = 0
for i in range(0, duz):
    j = i
    while broj[j+1] == "0" and j+1 < (duz):
        j = j + 1
    if tmp < j - i:
        tmp = j - i
        marker = i

print("The longest gap is", tmp, "it starts at position", marker)
