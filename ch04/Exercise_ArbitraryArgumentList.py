## This function will calculate the product of an argument list
## It will return 0 if no arguments are passed to it

def product(*args):
    productValue = 1
    for arg in args:
        productValue *= arg
    if (args):
        return productValue
    return 0

## Tests
print(f'The correct answer is 362880, product function answer is {product(1, 2, 3, 4, 5, 6, 7, 8, 9)}')
print(f'The correct answer is 1500, product function answer is {product(5, 3, 100)}')
print(f'The correct answer is 0, product function answer is {product()}')
