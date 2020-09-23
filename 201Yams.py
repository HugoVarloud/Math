#!/usr/bin/env python3

import sys
import math

FORMAT = {
	"pair" : "pair",
	"three" : "three-of-a-kind",
	"four" : "four-of-a-kind",
	}

def help():
	"""Display this help"""
	print("USAGE\n\t./201yams d1 d2 d3 d4 d5 c\n")
	print("DESCRIPTION\n\td1\tvalue of the first die (0 if not thrown)")
	print("\td2\tvalue of the second die (0 if not thrown)")
	print("\td3\tvalue of the third die (0 if not thrown)")
	print("\td4\tvalue of the fourth die (0 if not thrown)")
	print("\td5\tvalue of the fifth die (0 if not thrown)")
	print("\tc\texpected combination")
	sys.exit(84)

def bine(left, right):
	"""
	left : n (pop)
	right : k (sample)
	"""
	return (math.factorial(left) / (math.factorial(right) * math.factorial(left-right))) * pow(1/6, right) * pow(5/6, left-right)

def calcPr(v, w):
	"""calc proba for : pair, three, four, yams
	v: nb of elem wanted
	w: elem wanted
	"""
	result = 0
	nOccur = die.count(int(w))
	if nOccur >= v:
		return 1
	else:
		for i in range(v - nOccur, 6 - nOccur):
			result += bine(5 - nOccur, i)
	return result

def calcStraight(nlist, num):
	"""
	calc proba for : straight
	"""
	result = 0
	dice = set(nlist)
	if num == 5:
		dice.discard(6)
	elif num == 6:
		dice.discard(1)
	dice.discard(0)
	f = len(dice)
	for i in range(5 - f, 6 - f):
		result += bine(5 - f, i)
	return result

def calcFull(tre, dey, nlist):
	"""calc proba for : full"""
	result = 0
	treOccur = min(3, nlist.count(tre))
	deyOccur = min(2, nlist.count(dey))
	if treOccur == 3 and deyOccur == 2:
		return 1
	else:
		for i in range(5 - (treOccur + deyOccur), 6 - (treOccur + deyOccur)):
			result += bine(5 - (treOccur + deyOccur), i)
	return result * 10

def displayRes(name, dice, result):
	if name in FORMAT:
		name = FORMAT[name]
	print("chances to get a " + dice + " " + name + ": %.2f%%" % (result * 100))

def displayFull(name, dice1, dice2, res):
	print("chances to get a " + dice1 + " " + name + " of " + dice2 + ": %.2f%%" % (res * 100))


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
		sys.exit(84)
	try:
		combination = sys.argv[6]
		a = combination.split("_")
	except:
		print("Error : arg combination bad format...")
		sys.exit(84)
	die = list()
	try:
		nb_1 = int(sys.argv[1])
		if nb_1 < 0 or nb_1 > 6:
			print("Error : arg 1 invalid.")
			sys.exit(84)
		die.append(nb_1)
		nb_2 = int(sys.argv[2])
		if nb_2 < 0 or nb_2 > 6:
			print("Error : arg 2 invalid.")
			sys.exit(84)
		die.append(nb_2)		
		nb_3 = int(sys.argv[3])
		if nb_3 < 0 or nb_3 > 6:
			print("Error : arg 3 invalid.")
			sys.exit(84)
		die.append(nb_3)
		nb_4 = int(sys.argv[4])
		if nb_4 < 0 or nb_4 > 6:
			print("Error : arg 4 invalid.")
			sys.exit(84)
		die.append(nb_4)		
		nb_5 = int(sys.argv[5])
		if nb_5 < 0 or nb_5 > 6:
			print("Error : arg 5 invalid.")
			sys.exit(84)
		die.append(nb_5)
	except:
		sys.exit(84)
	if int(a[1]) < 1 or int(a[1]) > 6:
		print("Error : Combination format invalid.")
		sys.exit(84)
	if a[0] == "yams":
		displayRes("yams", a[1], calcPr(5, a[1]))
	if a[0] == "four":
		displayRes("four", a[1], calcPr(4, a[1]))
	if a[0] == "straight":
		if int(a[1]) == 5 or int(a[1]) == 6:
			displayRes("straight", a[1], calcStraight(die, a[1]))
		else:
			print("Error : Bad Straight format (5 or 6)")
			sys.exit(84)
	if a[0] == "full":
		if (int(a[2]) < 0 or int(a[2]) > 6):
			print("Error : Bad Full format")
			sys.exit(84)
		displayFull("full", a[1], a[2], calcFull(int(a[1]), int(a[2]), die))
	if a[0] == "three":
		displayRes("three", a[1], calcPr(3, a[1]))
	if a[0] == "pair":
		displayRes("pair", a[1], calcPr(2, a[1]))
	sys.exit(0)