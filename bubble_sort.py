#!/usr/bin/env python3

def bubbleSort(word_obj):
    '''Sorts list of word objects based on count in book'''
    for i in range(len(word_obj) - 1):
        for j in range(len(word_obj)-1):
            if word_obj[j].count >= word_obj[j+1].count:
                word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]

    reversed_word_obj = reversed(word_obj)
    return reversed_word_obj
