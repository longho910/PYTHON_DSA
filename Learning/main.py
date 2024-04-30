'''
# Variable and dynamically typed
n = 0
print('n = ', n)

# multiple assignment
n, m = 0, 'abc'
n, m, z = 0.125, "abc", False
print(n, m, z)

# increment
n = n + 1
n += 1  # cannot do n++



# None is null (absence of value)
n = 4
n = None
print('n = ', n)


# if statement don't need parenthesis
# or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
# parenthesis need for multiline condition
# and = &&
# or = ||
n, m = 1, 2
if ((n > 2 and
     n != m) or n == m):
    n += 1


# while loop are similar
n = 0
while n < 5:
    print(n)
    n += 1
    


# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

# Looping from 2 to 5
for i in range(2, 6):
    print(i)
   
# Looping from 5 to 2
for i in range(5, 1, -1):
    print(i)
    


# Division is decimal by default
print(5 / 2)  # 2.5

# Double slash rounds down
print(5.8 // 2)

# Careful: most language rounds toward 0
# python rounds DOWN for negative number
print(-3 // 2)  # -2

# workaround
print(int(-3/2))  # -1


# modding is similar to most language
import math
print(10 % 3)

# except for negative value
print(-10 % 3)  # 2

# to be consistent with other languages modulo
print(math.fmod(-10, 3))  # -1


# more math helper
import math
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(3/2))
print(math.pow(2,3))


# MIN/ Max int
float("inf")
float("-inf")

# python number are infinite so they're never overflow
import math
print(math.pow(2, 200))

print(math.pow(2,200) < float("inf"))


# Arrays called list in python
arr = [1, 2, 3]
print(arr)

# can be used as stack
arr.append(4)
arr.append(5)

print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)  # O(n)
print(arr)

arr[0] = 0  # O(1)
arr[3] = 0  # O(1)

print(arr)


# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
arr = [1,2,3,4,5]
print(arr)
print(len(arr))
print(arr[-1])
print(arr[-2])


nums = [1,2,3]

for i in range(len(nums)):
    print(nums[i])
    
for n in nums:
    print(n)

for i,n in enumerate(nums):
    print(i, n)
'''

# Loop through multiple arrays simultaneously
# using unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

# combine the pairs to be elt of array
# then unzip them
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
