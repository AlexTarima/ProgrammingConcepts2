# This code will check if the the data types set, bool, bytearray, str, range, int, and None are iterable

type_list = [set, bool, bytearray, str, range, int, None]

for type in type_list:
    print(hasattr(type, '__iter__'))
