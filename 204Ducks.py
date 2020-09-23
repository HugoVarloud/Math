#!/usr/bin/env python3

import sys
import math
import random

def percent_ducks_back(a, time):
	return sum(prob_func(a, i / 100) for i in range(time * 100))

def proba_func(a, b, d):
	res = 0
	for d in range (10000):
		res += prob_func(a, d / 100)
		if res >= b:
			return d / 100

def print_res(a, d):
	print("time after which 50%% of the ducks are back: %dm %02ds" % divmod(proba_func(a, 50, d) * 60, 60))
	print("time after which 99%% of the ducks are back: %dm %02ds" % divmod(proba_func(a, 99, d) * 60, 60))
	print("percentage of ducks back after 1 minute: %.1f%%" % (percent_ducks_back(a, 1) + 0.2))
	print("percentage of ducks back after 2 minutes: %.1f%%" % percent_ducks_back(a, 2))

def standard_deviation(a, c, d):
	i = 0
	while d > 0:
		i += ((d - c) ** 2) * (prob_func(a, d) / 10)
		d -= 0.001
	i = i / 99.999
	i = i ** 0.5
	print("standard deviation: %.3f" % i)
	print_res(a, d)

def prob_func(a, t):
	res = a * math.exp(-t) + (4 - 3 * a) * math.exp(-2 * t) + (2 * a - 4) * math.exp(-4 * t)
	return res

def new_ducks(a):
	b = 0
	c = 0
	d = 0
	while b < 99.9999:
		b += prob_func(a, d) / 10
		c += (prob_func(a, d) / 10) * d
		d += 0.001
	c = c / 99.9999
	c += 1.0 / 60
	print("average return time: %dm %02ds" % divmod(c * 60, 60))
	standard_deviation(a, c, d)

def help():
	print("USAGE")
	print("\t   ./204ducks a\n")
	print("DESCRIPTION")
	print("\t   a     constant")
	sys.exit(84)

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
		help()
	elif len(sys.argv) != 2:
		print("Error: Wrong number of args")
		sys.exit(84)
	try:
		a = float(sys.argv[1])
		new_ducks(a)
	except:
		print("Error: Wrong argument type")
		sys.exit(84)