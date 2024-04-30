'''
# pointer of integer (immutable)
num1 = 11  # num1 points to 11
num2 = num1 # num2 points to 11 that num1 points to

print("Before num2 value is updated")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# now, num2 points to different address that stores 22
# because integer is immutable (cannot be changed)
# so we cannot change value 11 that both num1 and num2 pointed to before
num2 = 22 

print("\nAfter num2 is updated")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
'''

# pointer of dictionary (mutable)
dict1 = {'value': 11}
dict2 = dict1  # dict2 will points to what dict1 points to, same as integer before

print("Before dict2 value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# this will change value of dict1 points to to 22
# because dictionary is mutable
dict2['value'] = 22 
print("\nAfter dict2 is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
