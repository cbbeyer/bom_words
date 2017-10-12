from bubble_sort import bubbleSort
from worddata import WordData
from insertion_sort import insertionSort
from selection_sort import selectionSort
from merge_api import merge_lists


words = []

w1 = WordData('1 Nephi', 'a', 7, 7)
words.append(w1)
w1 = WordData('1 Nephi', 'the', 3, 3)
words.append(w1)
w1 = WordData('1 Nephi', 'bravo', 1, 1)
words.append(w1)
w1 = WordData('1 Nephi', 'hi', 4, 4)
words.append(w1)
w1 = WordData('1 Nephi', 'alpha', 6, 6)
words.append(w1)
w1 = WordData('1 Nephi', 'delta', 2, 2)
words.append(w1)

sorted_words = insertionSort(words)

# for word in sorted_words:
#     print(word.word, word.count, word.percent)


words2 = []

w1 = WordData('4 Nephi', 'it', 1, 1)
words2.append(w1)
w1 = WordData('4 Nephi', 'this', 5, 5)
words2.append(w1)
w1 = WordData('4 Nephi', 'last', 9, 9)
words2.append(w1)
w1 = WordData('4 Nephi', 'death', 8, 8)
words2.append(w1)
w1 = WordData('4 Nephi', 'no', 7, 7)
words2.append(w1)
w1 = WordData('4 Nephi', 'store', 5, 5)
words2.append(w1)

sorted_words2 = insertionSort(words2)

# for word in sorted_words2:
#     print(word.word, word.count, word.percent)
#

merged_list = merge_lists(sorted_words, sorted_words2)

for word in merged_list:
    print(word.word, word.count, word.percent)
