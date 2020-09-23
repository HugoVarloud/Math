#!/usr/bin/env python3

import sys
import math
from time import time

def loibinom(cduration):
	i = 0
	callnum = 3500
	prob = cduration / (3600 * 8)
	calctime = time()
	res = 0
	print("Binomial distribution:")
	while i <= 50:
		cprob = (math.factorial(callnum) // (math.factorial(i) * math.factorial(callnum - i)) * (prob**i) * ((1 - prob)**(callnum - i)))
		print("%d -> %0.3f" %(i, cprob), end='')
		if i > 25:
			res = res + cprob
		i += 1
		if i % 6 != 0 and i != 51:
			print("\t", end='')
		if i % 6 == 0:
			print("")
	print("")
	print("overload: %.1f%%" % (res * 100))
	print("computation time: %.2f ms" % ((time() - calctime) * 1000))
	print("")

def loipoisson(cduration):
	i = 0
	prob = 3500 * (cduration / (3600 * 8))
	calctime = time()
	res = 0
	print("Poisson distribution:")
	while i <= 50:
		cprob = math.exp(-prob) * pow(prob, i) / math.factorial(i)
		print("%d -> %0.3f" %(i, cprob), end='')
		if i > 25:
			res = res + cprob
		i += 1
		if i % 6 != 0 and i != 51:
			print("\t", end='')
		if i % 6 == 0:
			print("")
	print("")
	print("overload: %.1f%%" % (res * 100))
	print("computation time: %.2f ms" % ((time() - calctime) * 1000))

def twoarg(n, k):
	nbis = math.factorial(n)
	kbis = math.factorial(k)
	nmoinsk = math.factorial(n - k)
	res = nbis // (kbis * nmoinsk)
	print(str(k) + "-combination of a " + str(n) + " set:")
	print(res)

def help():
	print("USAGE\n\t   ./203hotline [n k | d]\n\nDESCRIPTION")
	print("\t   n   n value for the computation of (n k)")
	print("\t   k   k value for the computation of (n k)")
	print("\t   d   average duration of calls (in seconds)")
	sys.exit(84)

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
		help()
	elif len(sys.argv) == 1:
		print("Error: Wrong number of args")
		sys.exit(84)
	elif len(sys.argv) == 2:
		try:
			cduration = int(sys.argv[1])
			loibinom(cduration)
			loipoisson(cduration)
		except:
			print("Error: Wrong argument")
			sys.exit(84)
	elif len(sys.argv) == 3:
		try:
			n = int(sys.argv[1])
			k = int(sys.argv[2])
			twoarg(n, k)
		except:
			print("Error: Wrong arguments")
			sys.exit(84)
	else:
		help()