# This program will tokenize an inputted sentence with split()
# It will then output some parts of it

sentence = input("Enter a sentence: ")
split_sentence = sentence.split()

# 1 - prints the reversed token list
print("Part 1 - the list of words, reversed")
print(split_sentence[::-1])

#2 - Prints if they begin on b
print("Part 2 - words beginning on b")
b_list = [token for token in split_sentence if token[0] == 'b']
print(b_list)

#3 - Prints if they end on ed
print("Part 3 - Words ending in ed")
ed_list = [token for token in split_sentence if token[-2:] == 'ed']
print(ed_list)