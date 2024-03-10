# This is a program to validate one of three date formats.
# If the date entered is valid, the program will calculate
# and print the date in all the formats.

import re

DEBUG = False  # Set to True if you want to execute debug statements
MONTHS = ("January","February","March","April","May","June","July","August",
          "September","October","November","December")

# Match mmddyy
# Note the use of raw (r"something") string format to eliminate the need for escape characters
REGEX1 = r"^(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])([0-9][0-9])$"
def validFmt1(date1):
    if (re.fullmatch(REGEX1, date1)):
        result = re.search(REGEX1, date1)
        if DEBUG: mm = result[1]  # Debug
        if DEBUG: dd = result[2]  # Debug
        if DEBUG: yy = result[3]  # Debug
        if DEBUG: print(f'function says mm = {mm} dd = {dd} yy = {yy}')   #Debug
        if DEBUG: print(f'function says {result.groups()}')  # Debug      
        return result.groups()
    else:
        return None
# Match mm/dd/yyyy    You need to implement this function
def validFmt2(date1):
    REGEX2 = r"^(0[1-9]|1[012])/(0[1-9]|[12][0-9]|3[01])/(19[0-9][0-9])$"
    if (re.fullmatch(REGEX2, date1)):
        result = re.search(REGEX2, date1)
        if DEBUG: mm = result[1]  # Debug
        if DEBUG: dd = result[2]  # Debug
        if DEBUG: yy = result[3]  # Debug
        if DEBUG: print(f'function says mm = {mm} dd = {dd} yy = {yy}')   #Debug
        if DEBUG: print(f'function says {result.groups()}')  # Debug      
        return result.groups()

# Match monthname dd, yyyy
def validFmt3(date1):
    REGEX3 = r"([A-Z][a-z]*)\s([0-3][0-9]),\s19(\d{2})"
    if (re.fullmatch(REGEX3, date1)):
        result = re.search(REGEX3, date1)
        if (result[1] in MONTHS):
            if DEBUG: mm = str(MONTHS.index(result[1]))  # Debug
            if DEBUG: dd = result[2]  # Debug
            if DEBUG: yy = result[3]  # Debug
            if DEBUG: print(f'function says mm = {mm} dd = {dd} yy = {yy}')   #Debug
            if DEBUG: print(f'function says {result.groups()}')  # Debug      
            return (str(MONTHS.index(result[1])), result[2], result[3])

#Print three formats from mm, dd, yy)
def printThreeFormats(mm, dd, yy):
    print(f'format 1 = {mm+dd+yy}')
    print(f'format 2 = {(mm + "/" + dd + "/" + "19" + yy)}')
    fmt3 = MONTHS[int(mm) - 1] + " " + dd + ", " + "19" + yy
    print(f'format 3 = {fmt3}')

def main():
    date = input('Enter date: ')
    # is date a valid format 1
    value1 = validFmt1(date)
    value2 = validFmt2(date)
    value3 = validFmt3(date)
    if value1 != None:
        printThreeFormats(value1[0], value1[1], value1[2])
        if DEBUG: print(f'Main says {value1}, {value2}, {value3}') # Debug
    elif value2 != None:
        printThreeFormats(value2[0], value2[1], value2[2])
        if DEBUG: print(f'Main says {value1}, {value2}, {value3}') # Debug
    elif value3 != None:
        printThreeFormats(value3[0], value3[1], value3[2])
        if DEBUG: print(f'Main says {value1}, {value2}, {value3}') # Debug
    else:
        print(f'{date} is not valid date')
    # Don't forget this logic structure must be modified to test the other two formats and say not valid 
    # only if date does not match any of the formats
main()
