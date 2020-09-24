# Question 2
coordinates = [("f", 9), ("z", 2), ("t", 4), ("x", 8), ("b", 1), ("m", 7)]
first_list = [coord[0] for coord in coordinates]
first_list.sort()
first_sorted = []
for item in first_list:
    for coord in coordinates:
        if coord[0] == item:
            first_sorted.append(coord)
print(first_sorted)

second_list = [coord[1] for coord in coordinates]
second_list.sort()
second_sorted = []
for item in second_list:
    for coord in coordinates:
        if coord[1] == item:
            second_sorted.append(coord)
print(second_sorted)

# Question 4
from math import log2

elements = 500000
quicksort = elements * elements
mergesort = elements * log2(elements)
division = quicksort / mergesort
print("Quicksort is %i times faster than merge sort." % division)

# Question 6
sentence = input("Write a sentence: ")
words = sentence.split(" ")
print("There are %i words in the sentence." % len(words))
