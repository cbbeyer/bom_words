#!/usr/bin/env python3

def insertionSort(word_obj):
    '''Sorts list of word objects based on count in book'''
    for i in range(1, len(word_obj)):
        j = i - 1
        while word_obj[j].count > word_obj[j+1].count and j >= 0:
            word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]
            j -= 1

    reversed_word_obj = reversed(word_obj)
    return reversed_word_obj
