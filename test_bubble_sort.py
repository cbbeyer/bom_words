from bubble_sort import bubbleSort
from worddata import WordData
from insertion_sort import insertionSort


words = []

w1 = WordData('1 Nephi', 'the', 15, 5)
words.append(w1)
w1 = WordData('1 Nephi', 'a', 3, 2)
words.append(w1)
w1 = WordData('1 Nephi', 'to', 2, 1)
words.append(w1)
w1 = WordData('1 Nephi', 'hi', 10, 3.25)
words.append(w1)
w1 = WordData('1 Nephi', 'test', 11, 3.5)
words.append(w1)
w1 = WordData('1 Nephi', 'like', 14, 4.5)
words.append(w1)

sorted_words = insertionSort(words)

for word in sorted_words:
    print(word.word, word.count)
