#!/usr/bin/python

from random import randrange, sample

# inputs
corpus_path = input("Path to text file, in quotes: ")
words_lower_limit = input("Words-per-line lower limit: ")
words_upper_limit = input("Words-per-line upper limit: ")
lines_lower_limit = input("Total lines lower limit: ")
lines_upper_limit = input("Total lines upper limit: ")

total_lines = randrange(int(lines_lower_limit),int(lines_upper_limit))

# open corpus from file and read into memory
corpus = open(corpus_path, 'rt')
data = corpus.read()

# make each word an item in an array
wordlist = data.split()

for i in range(0, total_lines) : 
    poem = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
    print(poem)
