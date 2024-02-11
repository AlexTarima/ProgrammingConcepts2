## This program will sum the triples of even numbers of 1 through 10
## It will do so through sum, filter, and map together
## It will also do so through a list comprehension

example = list(range(1,11))
sum_mfr = sum(map(lambda x: x*3, filter(lambda x: x % 2 == 0, example)))
sum_lc = sum([val * 3 for val in example if val % 2 == 0])

print("The sum from using map, filter, and sum is: ", sum_mfr)
print("The sum from using list comprehension is: ", sum_lc)