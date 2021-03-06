#!/usr/bin/python

# enhancements:
# - add at end an option to restart, ie, input all new paramenters
# - input ranges in "A-B" format, or allow specific number
# - automatically populate text input options, based on contents of texts/

from random import randrange, sample

# inputs
# corpus_name = raw_input("File name, with extension: ")
print("")
print("")
print("  #=#=# Welcome to the Poem-Machine #=#=#")
print("")
print("")
print("  Choose an input text: ")
print("")
print("           1: Dickinson's Poems")
print("           2: Thoreau's Journal")
print("           3: Fuller's Summer on the Lakes")
print("           4: U.S. Constitution")
print("           5: The Canterbury Tales")
print("           6: Custom")
print("")

inp = int(input("Enter a number: "))
if inp == 1:
    corpus_name = "dickinson.txt"
elif inp == 2:
    corpus_name = "thoreau.txt"
elif inp == 3:
    corpus_name = "fuller.txt"
elif inp == 4:
    corpus_name = "constitution.txt"
elif inp == 5:
    corpus_name = "canterbury.txt"
elif inp == 6:
    corpus_name = raw_input("Enter file name, with extension: ")
else:
    print("Invalid input!")
    exit

print("")
words_lower_limit = input("Words-per-line lower limit: ")
words_upper_limit = input("Words-per-line upper limit: ")
lines_lower_limit = input("Total lines lower limit: ")
lines_upper_limit = input("Total lines upper limit: ")


total_lines = randrange(int(lines_lower_limit),int(lines_upper_limit))

corpus_path = "texts/{}".format(corpus_name)



# open corpus from file and read into memory
with open(corpus_path, 'rt') as corpus:
    
    data = corpus.read()
    
    # make each word an item in an array
    wordlist = data.split()

while True:
    print("")
    print("")
    print("   ====POEM====")
    print("")
    
    for i in range(0, total_lines) : 
        line = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
        print(line)  
        
    print("")
    print("     =======")
    print("")


    # print("What would you like to do?")
    # print("   1: Run again with same parameters")
    # print("   2: Exit program")
    # print("")

    inp = raw_input("One more time? (y/n): ")
    if inp == "y":
        continue
    else:
        print("")
        print("See you next time!")
        print("")
        break
