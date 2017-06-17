#!/usr/bin/env python3

import random

afile = open("zasort.txt", "w" )

granica = int(input('Random from 1 to ?  '))
iteracija = int(input('How many random numbers?: '))

for i in range(iteracija):
    line = str(random.randint(1, granica))
    afile.write(line)
    afile.write(' ')
    print(line)

afile.close()
