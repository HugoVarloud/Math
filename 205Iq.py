#!/usr/bin/env python3

import sys
import math

def formula_one(arg1, arg2, i):
	return (1 / (float(arg2) * math.sqrt(2 * math.pi))) * math.exp(-0.5 * pow((float(i) - float(arg1)) / float(arg2), 2))

def set_tab(arg1, arg2):
	i = 0
	res = 0.0
	while i < 201:
		res = (1 / (float(arg2) * math.sqrt(2 * math.pi))) * math.exp(-0.5 * pow((float(i) - float(arg1)) / float(arg2), 2))
		tab.append(res * 100)
		i += 1

def fourarg(arg1, arg2, arg3, arg4):
	i = 1.0 * arg3
	res = 0.0
	while i < arg4:
		res = res + formula_one(arg1, arg2, i)
		i += 0.01
	print("%0.1f%% of people have an IQ between %d and %d" % (res, arg3, arg4))

def threearg(arg1, arg2, iq):
	i = 0.0
	res = 0.0
	while i < iq:
		res = res + formula_one(arg1, arg2, i)
		i += 0.01
	print("%0.1f%% of people have an IQ inferior to %d" % (res, iq))

def twoarg(arg1, arg2):
	set_tab(arg1, arg2)
	i = 1
	while i < 201:
		if tab[i] < 0:
			sys.exit(84)
		print("%d %0.2f" % (i, tab[i]))
		i += 1

def help():
	print("USAGE")
	print("\t   ./205IQ μ σ [IQ1] [IQ2]\n")
	print("DESCRIPTION")
	print("\t   μ    preditermined area")
	print("\t   σ    preditermined standard deviation")
	print("\t   [IQ1] minimum IQ")
	print("\t   [IQ2] maximum IQ")
	sys.exit(84)

if __name__ == "__main__":
	tab = list()
	if len(sys.argv) == 1:
		print("Error: wrong number of args")
		sys.exit(84)
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
		help()
	if len(sys.argv) == 2:
		print("Error: wrong number of args")
		sys.exit(84)
	elif len(sys.argv) > 5:
		print("Error: wrong number of args")
		sys.exit(84)
	elif len(sys.argv) == 3:
		try:
			arg1 = int(sys.argv[1])
			arg2 = int(sys.argv[2])
			if arg1 != 100 or arg2 <= 0:
				sys.exit(84)
			twoarg(arg1, arg2)
		except:
			print("Error: wrong arguments")
			sys.exit(84)
	elif len(sys.argv) == 4:
		try:
			arg1 = int(sys.argv[1])
			arg2 = int(sys.argv[2])
			iq = int(sys.argv[3])
			if arg1 != 100 or arg2 <= 0:
				sys.exit(84)
			if iq > 200 or iq < 0:
				sys.exit(84)
			threearg(arg1, arg2, iq)
		except:
			print("Error: wrong arguments")
			sys.exit(84)
	elif len(sys.argv) == 5:
		try:
			arg1 = int(sys.argv[1])
			arg2 = int(sys.argv[2])
			arg3 = int(sys.argv[3])
			arg4 = int(sys.argv[4])
			if arg1 != 1000 or arg2 <= 0:
				sys.exit(84)
			if arg3 > 200 or arg3 < 0:
				sys.exit(84)
			if arg4 > 200 or arg4 < 0:
				sys.exit(84)
			if arg3 > arg4:
				sys.exit(84)
			fourarg(arg1, arg2, arg3, arg4)
		except:
			print("Error: wrong arguments")
			sys.exit(84)
	sys.exit(0)