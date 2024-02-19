## This program will test various set operands
## It will print the results to the console

result = {}
result = {1, 2, 4, 8, 16} - {1, 4, 16, 64, 256} # {2,8}, difference
print(result)
result = {1, 2, 4, 8, 16} & {1, 4, 16, 64, 256} # {1,4,16}, intersection
print(result)
result = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256} # {1,2,4,8,16,64,256}, union
print(result)
result = {1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256} # {2,8,64,256}, symmetric difference
print(result)
result = {1, 2, 4, 8, 16} <= {1, 4, 16, 64, 256} # False, improper subset
print(result)