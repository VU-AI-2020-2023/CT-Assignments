# Question 2
coordinates = [("f", 9), ("z", 2), ("t", 4), ("x", 8), ("b", 1), ("m", 7)]
list_A = [coord[0] for coord in coordinates]
list_A.sort()
sorted_A = []
for item in list_A:
    for coord in coordinates:
        if coord[0] == item:
            sorted_A.append(coord)
print(sorted_A)

list_B = [coord[1] for coord in coordinates]
list_B.sort()
sorted_B = []
for item in list_B:
    for coord in coordinates:
        if coord[1] == item:
            sorted_B.append(coord)
print(sorted_B)

# Question 4
from math import log2

elements = 500000
quicksort = elements * elements
mergesort = elements * log2(elements)
times_faster = quicksort / mergesort
print("Quicksort is %i times faster than merge sort." % times_faster)

# Question 6
sentence = input("Write a sentence: ")
words = sentence.split(" ")
print("There are %i words in the sentence." % len(words))
