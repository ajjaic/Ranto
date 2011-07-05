#!/usr/bin/python2

import random
import sys

def topics(f):
	f = open(f, 'r')
	wordlist = []

	for i in f:
		wordlist.append(i.strip())
	return wordlist

def mainp():
	wordlist = topics('../data/' + sys.argv[1])
	
	while True:
		print random.sample(wordlist, int(sys.argv[2]))
		if raw_input() == '':
			continue
		else:
			break	

mainp()
