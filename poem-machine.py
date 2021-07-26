#!/usr/local/bin/python3

# todos/enhancements:
# - input ranges in "A-B" format, or allow specific number
# - automatically populate text input options, based on contents of texts/
# - include error detection on invalid inputs
#   - check if custom file exists
#   - check if limits are integers
#   - check if upper limits are greater than lower limits
#     - print("You must enter a number greater than {}.".format(words_lower_limit))
#     - print("You must enter a number greater than {}.".format(lines_lower_limit))
# + add end option to repeat, restart, or exit
# + add poem count
# + add error detection to initial text input
# + tidy formatting

from random import randrange, sample

while True:
    print("\n===================================================")
    print("\n      #=#=# Welcome to the Poem-Machine #=#=#\n")

    print(" Choose an input text: \n")

    print("        1: Dickinson's Poems")
    print("        2: Thoreau's Journal")
    print("        3: Fuller's Summer on the Lakes")
    print("        4: U.S. Constitution")
    print("        5: The Canterbury Tales")
    print("        6: Custom\n")

    while True:
        inp = input("Enter a number: ")
        if inp == "1":
            corpus_name = "dickinson.txt"
            corpus_title = "Dickinson's poems"
            break
        elif inp == "2":
            corpus_name = "thoreau.txt"
            corpus_title = "Thoreau's journal"
            break
        elif inp == "3":
            corpus_name = "fuller.txt"
            corpus_title = "Fuller's _Summer on the Lakes_"
            break
        elif inp == "4":
            corpus_name = "constitution.txt"
            corpus_title = "the U.S. Constitution"
            break
        elif inp == "5":
            corpus_name = "canterbury.txt"
            corpus_title = "the Canterbury Tales"
            break
        elif inp == "6":
            corpus_name = input("Enter file name, with extension: ")
            corpus_title = corpus_name
            break
        else:
            print("Invalid input.")

    print("\nYou've chosen: {}\n".format(corpus_title))

    words_lower_limit = input("Words-per-line lower limit: ")
    words_upper_limit = input("Words-per-line upper limit: ")
    lines_lower_limit = input("Total lines lower limit: ")
    lines_upper_limit = input("Total lines upper limit: ")

    total_lines = randrange(int(lines_lower_limit),int(lines_upper_limit))

    corpus_path = "texts/{}".format(corpus_name)

    count = 1

    # open corpus from file and read into memory
    with open(corpus_path, 'rt') as corpus:
    
        data = corpus.read()
    
        # make each word an item in an array
        wordlist = data.split()

    def churn_lines():
        print("\n\n\n    ==== POEM {} ====\n".format(count))
    
        for i in range(0, total_lines) : 
            line = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
            print(line)  
  
        print("\n      ==========")

    churn_lines()

    while True:
        print("\nPress <Enter> for another poem.")
        inp = input("  Or type 'r' to restart, or 'q' to quit: ")
        if inp == "":
            count = count +1
            churn_lines()
        elif inp == "r":
            break
        elif inp == "q":
            print("\nAlright then, see ya!\n")
            exit()
        else:
            print("\nInvalid input.")
            continue
