## This program will calculate if a string is a palindrome
## Case, spaces, and punctuation are not included in the calculations

stack = []

def is_palindrome(pal):
    pal = pal.lower()
    alphabetical_letters = filter(str.isalpha, pal)
    pal = ''.join(alphabetical_letters)
    stack = []
    for i in pal:
        stack.append(i)
    for i in pal:
        if (i == stack.pop()):
            continue
        else:
            return False
        
    return True


print(f"Monday is not a palindrome, is_palindrome says {is_palindrome('Monday')}")
print(f"able was i ere I Saw elba is a palindrome, is_palindrome says {is_palindrome('able was i ere I Saw elba')}")
print(f"radar is a palindrome, is_palindrome says {is_palindrome('radar')}")
print(f"able was i, ere I Saw elba: is a palindrome, is_palindrome says {is_palindrome('able was i, ere I Saw elba:')}")
