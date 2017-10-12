#!/usr/bin/env python3

def selectionSort(word_obj):
    '''Sorts list of word objects based on count in book'''
    for i in range(len(word_obj)-1):
        min_index = i

        for t in range(i+1, len(word_obj)):
            if word_obj[t].count < word_obj[min_index].count:
                min_index = t
            elif word_obj[t].count == word_obj[min_index].count:
                # alphabetical order if the counts are the same
                str_comp = []
                str_comp.append(word_obj[t].word)
                str_comp.append(word_obj[min_index].word)
                str_comp.sort()
                if word_obj[t].word != str_comp[0]:
                    min_index = t

        if min_index != i:
            word_obj[i], word_obj[min_index] = word_obj[min_index], word_obj[i]

    # reversed_word_obj = reversed(word_obj)
    # return reversed_word_obj
    return word_obj
