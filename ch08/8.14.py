# This program will output words beginning/ending on b/ed
# It will use regular expressions to do so

import re

sentence = input("Enter a sentence: ")
split_sentence = sentence.split()

#2 - Prints if they begin on b

print("Part 2 - words beginning on b")
b_list = re.findall(r'\bb\w*', sentence)
print(b_list)

#3 - Prints if they end on ed
print("Part 3 - Words ending in ed")
ed_list = re.findall(r'\b\w+ed\b', sentence)
print(ed_list)