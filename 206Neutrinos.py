#!/usr/bin/env python3

import sys
import math

def standard_input():
	print("indtast din vaerdi :  ", end='')
	user = input()
	if user == "ENDE":
		exit(0)
	else:
		try:
			num = float(user)
		except:
			print("Error: input must be a positive number")
			sys.exit(84)
	if num < 0 or num == 0:
		print("Error: input must be a positive number")
		sys.exit(84)
	return num

def quik_maffs(n, a, h, sd):
	user = standard_input()
	b = n * a
	scoef = (sd**2 + a**2) * n
	n = n + 1
	a = (b + user) / n
	kva = math.sqrt((scoef + user**2) / n)
	h = n / (1 / user + (n - 1) / h)
	sd = math.sqrt((scoef + user**2) / n - a**2)
	print("     antal mãlinder :\t     %i" % n)
	print("     standardafvilgelse :    %.2f" % sd)
	print("     aritmetisk gennemsnit : %.2f" % a)
	print("     kvadratisk gennemsnit : %.2f" % kva)
	print("     harmonisk gennemsnit :  %.2f\n" % h)
	quik_maffs(n, a, h, sd)

def help():
	print("USAGE")
	print("\t   ./206neutrinos n a h sd\n")
	print("DESCRIPTION")
	print("\t   n    number of values")
	print("\t   a    arithmetic mean")
	print("\t   h    harmonic mean")
	print("\t   sd   standard deviation")
	sys.exit(84)
	sys.exit(0)

if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "-h":
		help()
	elif len(sys.argv) != 5:
		print("Error: wrong agruments")
		sys.exit(84)
	try:
		n = float(sys.argv[1])
		a = float(sys.argv[2])
		h = float(sys.argv[3])
		sd = float(sys.argv[4])
		if n < 0 or a < 0 or h < 0 or sd < 0:
			print("Error: arguments must be positive")
			sys.exit(84)
	except:
		print("Error: bad arguments")
		sys.exit(84)
	quik_maffs(n, a, h, sd)