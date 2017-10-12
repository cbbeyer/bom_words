#!/usr/bin/env python3

def merge_lists(listA, listB):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''

    a_count = 0
    b_count = 0
    merged_list = []

    while a_count < len(listA) and b_count < len(listB):
        if listA[a_count].percent < listB[b_count].percent:
            merged_list.append(listA[a_count])
            a_count += 1
        # elif listA[a_count].percent > listB[b_count].percent:
        else:
            merged_list.append(listB[b_count])
            b_count += 1
        # elif listA[a_count].percent == listB[b_count].percent:
        #     str_comp = []
        #     str_comp.append(listA[a_count].word)
        #     str_comp.append(listB[b_count].word)
        #     str_comp.sort()
            # if word_obj[j].word == str_comp[0]:
            #     pass

    while a_count < len(listA):
        merged_list.append(listA[a_count])
        a_count += 1

    while b_count < len(listB):
        merged_list.append(listB[b_count])
        b_count += 1

    return merged_list
