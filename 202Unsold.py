#!/usr/bin/env python3

import sys

def help():
	""" Fonction qui va afficher l'aide. """
	print("USAGE\n\t   ./202unsold a b\n\nDESCRIPTION\n\t   a   constant computed from the past results")
	print("\t   b   constant computed from the past result")
	sys.exit(84)

def error_int(a):
	""" Fonction qui check si les arguments sont des ints. """
	try:
		i = int(a)
		return i
	except ValueError:
		return None
def error():
	""" Fonction en charge de la gestion d'erreur. """
	args = []
	if (len(sys.argv)) == 3:
		for a in sys.argv[1:3]:
			args.append(error_int(a))
		for a in args:
			if a == None or a < 50:
				return 84
		return args
	return 84


def jointLaw(a, b):
	""" Fonction qui performe le calcul. sans arrondir """
	l1 = [i for i in [10, 20, 30, 40, 50]]
	res = [[((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150)) for x in l1] for y in l1]
	return res

def jointLawRound(a, b):
	""" Fonction qui performe le calcul. """
	l1 = [10, 20, 30, 40, 50]
	res = [[round(((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150)), 3) for x in l1] for y in l1]
	return res

def displayJointLaw(a):
	""" Fonction qui affiche la table des resultat pour la joint Law. """
	print('-' * 61)
	print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
	f = 10
	for i in a:
		print('Y=%s\t%s' % (str(f), '\t'.join(map(str, i))), end='')
		print("\t%.3f" % sum(i))
		f += 10
	print("X law \t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t1" % ((a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[4][0]),
							  (a[0][1] + a[1][1] + a[2][1] + a[3][1] + a[4][1]),
							  (a[0][2] + a[1][2] + a[2][2] + a[3][2] + a[4][2]),
							  (a[0][3] + a[1][3] + a[2][3] + a[3][3] + a[4][3]),
							  (a[0][4] + a[1][4] + a[2][4] + a[3][4] + a[4][4])))
	print('-' * 61)

def variance(expected, start, a):
	res = 0
	z = {'expected_x': expected_x,
		'expected_y': expected_y,
		'expected_z': expected_z,
	}
	e = {'expected_x': [(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[4][0]),
		  (a[0][1] + a[1][1] + a[2][1] + a[3][1] + a[4][1]),
		  (a[0][2] + a[1][2] + a[2][2] + a[3][2] + a[4][2]),
		  (a[0][3] + a[1][3] + a[2][3] + a[3][3] + a[4][3]), 
		(a[0][4] + a[1][4] + a[2][4] + a[3][4] + a[4][4])],
	     'expected_y': [(a[0][0] + a[0][1] + a[0][2] + a[0][3] + a[0][4]),
		  (a[1][0] + a[1][1] + a[1][2] + a[1][3] + a[1][4]),
		  (a[2][0] + a[2][1] + a[2][2] + a[2][3] + a[2][4]),
		  (a[3][0] + a[3][1] + a[3][2] + a[3][3] + a[3][4]),
		  (a[4][0] + a[4][1] + a[4][2] + a[4][3] + a[4][4])],
	     'expected_z': [(b[0][0]),
		  (b[1][0] + b[0][1]),
		  (b[2][0] + b[1][1] + b[0][2]),
		  (b[3][0] + b[2][1] + b[1][2] + b[0][3]),
		  (b[4][0] + b[3][1] + b[2][2] + b[1][3] + b[0][4]),
		  (b[4][1] + b[3][2] + b[2][3] + b[1][4]),
		  (b[4][2] + b[3][3] + b[2][4]),
		  (b[4][3] + b[3][4]),
		  (b[4][4])],
		}
	mult = start
	for nb in e[expected]:
		res += nb * ((mult - z[expected](a)) ** 2)
		mult += 10
	return res

def expected_z(a):
	return ((b[0][0]) * 20
		+  (b[1][0] + b[0][1]) * 30
		+  (b[2][0] + b[1][1] + b[0][2]) * 40
		+  (b[3][0] + b[2][1] + b[1][2] + b[0][3]) * 50
		+  (b[4][0] + b[3][1] + b[2][2] + b[1][3] + b[0][4]) * 60
		+  (b[4][1] + b[3][2] + b[2][3] + b[1][4]) * 70
		+  (b[4][2] + b[3][3] + b[2][4]) * 80
		+  (b[4][3] + b[3][4]) * 90
		+  (b[4][4] * 100))

def expected_y(a):
	return ((a[0][0] + a[0][1] + a[0][2] + a[0][3] + a[0][4]) * 10
		    + (a[1][0] + a[1][1] + a[1][2] + a[1][3] + a[1][4]) * 20
		    + (a[2][0] + a[2][1] + a[2][2] + a[2][3] + a[2][4]) * 30
		    + (a[3][0] + a[3][1] + a[3][2] + a[3][3] + a[3][4]) * 40
		    + (a[4][0] + a[4][1] + a[4][2] + a[4][3] + a[4][4]) * 50)
def expected_x(a):
	return ((a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[4][0]) * 10
		+ (a[0][1] + a[1][1] + a[2][1] + a[3][1] + a[4][1]) * 20
		+ (a[0][2] + a[1][2] + a[2][2] + a[3][2] + a[4][2]) * 30
		+ (a[0][3] + a[1][3] + a[2][3] + a[3][3] + a[4][3]) * 40
		+ (a[0][4] + a[1][4] + a[2][4] + a[3][4] + a[4][4]) * 50)

if __name__ == "__main__":
	args = error()
	if "-h" in sys.argv:
		help()
	if args is 84:
		print("Error : argument error.")
		sys.exit(84)
	a = jointLawRound(args[0], args[1])
	displayJointLaw(a)
	print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\tto")
	print("p(Z=z)\t", end='')
	b = jointLaw(args[0], args[1])
	print("%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t1" % ((b[0][0]), 
						  (b[1][0] + b[0][1]),
						  (b[2][0] + b[1][1] + b[0][2]),
						  (b[3][0] + b[2][1] + b[1][2] + b[0][3]),
						  (b[4][0] + b[3][1] + b[2][2] + b[1][3] + b[0][4]),
						  (b[4][1] + b[3][2] + b[2][3] + b[1][4]),
						  (b[4][2] + b[3][3] + b[2][4]),
						  (b[4][3] + b[3][4]),
						  (b[4][4]),))
	print('-' * 61)
	print("expected value of X:\t%.1f" % (expected_x(a)))
	print("variance of X:\t%.1f" % variance("expected_x", 10, a))
	print("expected value of Y:\t%.1f" % (expected_y(a)))
	print("variance of Y:\t%.1f" % variance("expected_y", 10, a))
	print("expected value of Z:\t%.1f" % (expected_z(a)))
	print("variance of Z:\t%.1f" % variance("expected_z", 20, a))
	print('-' * 61)