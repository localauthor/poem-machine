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
print("         1: Dickinson's Poems")
print("         2: Thoreau's Journal")
print("         3: Fuller's Summer on the Lakes")
print("         4: U.S. Constitution")
print("         5: The Canterbury Tales")
print("         6: Custom")
print("")

inp = int(input("Enter a number: "))
if inp == 1:
    corpus_name = "dickinson.txt"
    corpus_title = "Dickinson's poems"
elif inp == 2:
    corpus_name = "thoreau.txt"
    corpus_title = "Thoreau's journal"
elif inp == 3:
    corpus_name = "fuller.txt"
    corpus_title = "Fuller's _Summer on the Lakes_"
elif inp == 4:
    corpus_name = "constitution.txt"
    corpus_title = "the U.S. Constitution"
elif inp == 5:
    corpus_name = "canterbury.txt"
    corpus_title = "the Canterbury Tales"
elif inp == 6:
    corpus_name = raw_input("Enter file name, with extension: ")
    corpus_title = "a text of your choosing"
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
    print("Based on {}:").format(corpus_title)
    print("")
    print("      ====POEM====")
    print("")
    
    for i in range(0, total_lines) : 
        line = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
        print(line)  
        
    print("")
    print("        ========")
    print("")

    print("Press <Enter> for another poem.")
    
    inp = raw_input("Or type 'q' to quit: ")
    if inp == "":
        continue
    if inp == "y":
        continue
    else:
        print("")
        print("See you next time!")
        print("")
        break
