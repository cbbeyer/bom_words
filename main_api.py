#!/usr/bin/env python3
import sys, re
from merge_api  import merge_lists
from worddata import WordData
from bubble_sort import bubbleSort
from insertion_sort import insertionSort

FILENAMES = [
    [ '1 Nephi',         '01-1 Nephi.txt' ],
    [ '2 Nephi',         '02-2 Nephi.txt' ],
    [ 'Jacob',           '03-Jacob.txt' ],
    [ 'Enos',            '04-Enos.txt' ],
    [ 'Jarom',           '05-Jarom.txt' ],
    [ 'Omni',            '06-Omni.txt' ],
    [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    [ 'Mosiah',          '08-Mosiah.txt' ],
    [ 'Alma',            '09-Alma.txt' ],
    [ 'Helaman',         '10-Helaman.txt' ],
    [ '3 Nephi',         '11-3 Nephi.txt' ],
    [ '4 Nephi',         '12-4 Nephi.txt' ],
    [ 'Mormon',          '13-Mormon.txt' ],
    [ 'Ether',           '14-Ether.txt' ],
    [ 'Moroni',          '15-Moroni.txt' ],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    # lowercase the entire text
    with open(text, 'r') as f:
        all_words = f.read()
        all_words = all_words.lower()

    # split the text by whitespace to get a list of words
    string_file = re.split('\s+', all_words)
    words = []

    for i in string_file:
        new_i = re.findall("[a-z]+", i)
        if len(new_i) > 1:

            # convert each word to the longest run of characters
            if len(new_i[0]) >= len(new_i[1]):
                del new_i[1]
            else:
                del new_i[0]

        # eliminate any words that are empty after conversion to characters
        if new_i:
            words.append(new_i)

    # count up the occurance of each word into a dictionary of: word -> count
    agg_words = {}
    for w in words:
        if w[0] in agg_words:
            temp_count = agg_words[w[0]]
            temp_count += 1
            agg_words[w[0]] = temp_count
        else:
            agg_words[w[0]] = 1

    # create a WordData item for each word in our list of words
    word_objects = []

    for key in agg_words:
        wordData = WordData(book, key, agg_words[key], agg_words[key]/len(words)*100)
        word_objects.append(wordData)

    # print out words over certain threshold - MAYBE DO THIS IN MAIN() ?????
    # print_words(word_objects, 2)
    # print()

    # sorted_words = bubbleSort(word_objects)
    sorted_words = insertionSort(word_objects)

    if text == '01-1 Nephi.txt':
        print_words(sorted_words)
        print()
    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]

    # return

################################
###   Prints a words list

def print_words(words, threshold=None, word=None):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word
    # if threshold is not None:
    for word in words:
        if threshold is not None:
            if word.percent > threshold:
                print(word.book, word.word, word.count, format(word.percent, '.1f'))
        else:
            print(word.book, word.word, word.count, format(word.percent, '.1f'))
    # else:
    #     print(format(word.percent, '.1f'), word.word)



    # print an empty line



#######################
###   Main loop

def main():
    '''Main program'''
    master = []
    # loop through the filenames and analyze each one
    print('INDIVIDUAL BOOKS > 2%')
    for i in range(len(FILENAMES)):
        analyze_text(FILENAMES[i][0], FILENAMES[i][1])
        # ADD TO MASTER
    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)


    # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')

    # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')

    # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')



#######################
###   Runner

if __name__ == '__main__':
    main()
