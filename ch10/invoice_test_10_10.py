#This program will perform 4 exercises using the Invoice class

from invoice_class_10_10 import Invoice

#1
print("#1")
invoice1 = Invoice("part_number", "part_description", 10, 1)
print(invoice1)

#2
print("#2")
try:
    invoice2 = Invoice("part_number", "part_description", -10, 1)
except ValueError as error:
    print(error)

#3
print("#3")
try:
    invoice3 = Invoice("part_number", "part_description", 10, -1)
except ValueError as error:
    print(error)

#4
print("#4")
invoice1.part_number = "10"
invoice1.part_description = "changed part description"
invoice1.quantity = 2
invoice1.price_per_item = 10
print(invoice1)




