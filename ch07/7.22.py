# This program will use the capabilities of Panda's series
# It will print the results of the tests in a readable format

import pandas as pd
import random

# A
print("Section A")
section_a = pd.Series([7,11,13,17])
print("The series created in Section A is")
print(section_a)
# B
print('')
print("Section B")
section_b = pd.Series(100.0, range(5))
print("The series created in Section B is")
print(section_b)
# C
print('')
print("Section C")
section_c = pd.Series([random.uniform(0,100) for _ in range(20)])
print("The statistics of the series of 20 random numbers between 0 and 100 in Section C is")
print(section_c.describe())
#D
print('')
print("Section D")
section_d = pd.Series([98.6, 98.9, 100.2, 97.9], index=["Julie", "Charlie", "Sam", "Andrea"])
print("The result of Section D is")
print(section_d)
#E
dictionary_e = {'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9}
section_e = pd.Series(dictionary_e)
print('')
print("The result of Section E is")
print(section_e)
