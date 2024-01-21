# This program will create a word index txt file. 
# This file will containcontain an alphabetical listing of the words that are stored as keys in the dictionary, 
# along with the line numbers where the words appear in the original file.

import os

def word_indexer(input_file, output_file) :
    dictionary = {}

    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        lines[i] = line.strip().lower().split()
    
    for i, line in enumerate(lines):
        for word in line:
            if word:
                if word in dictionary:
                    dictionary[word].append(i + 1)
                else:
                    dictionary[word] = [i + 1]

    with open(output_file, 'w') as file:
        for word in dictionary:
            file.write(word + ": " + ' '.join(list(map(str, dictionary.get(word)))))
            if word != list(dictionary.keys())[-1]:
                file.write('\n')

word_indexer('Longfellow.txt', 'index.txt')