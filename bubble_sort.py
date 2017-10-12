#!/usr/bin/env python3

def bubbleSort(word_obj):
    '''Sorts list of word objects based on count in book'''
    for i in range(len(word_obj) - 1):
        for j in range(len(word_obj)-1):
            if word_obj[j].count > word_obj[j+1].count:
                word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]
            elif word_obj[j].count == word_obj[j+1].count:
                # alphabetical order if the counts are the same
                str_comp = []
                str_comp.append(word_obj[j].word)
                str_comp.append(word_obj[j+1].word)
                str_comp.sort()
                if word_obj[j].word == str_comp[0]:
                    word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]

    # reversed_word_obj = reversed(word_obj)
    # return reversed_word_obj
    return word_obj
