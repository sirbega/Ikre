#!/usr/bin/env python3

def convert(s):
	try:
		x = int(s)
		print(factorial(x))
	except (ValueError, TypeError, NameError) as e:
		print('Input number!')
		afile = open("greske.txt", "a" )
		afile.write(str(e))
		afile.write('\n')
		afile.close()

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

unos = input('Input number for which I should calculate factorial: ')
convert(unos)
