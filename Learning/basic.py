'''
# variables are dynamically typed
n = 0
print(n)
n = 'abc'
print(n)

# multiple assignments
n, m = 0, 'abc'
n, m, z = 0.125, 'abc', False

# increment
n = n  + 1
n += 1

# None is null (absence of value)


# if
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2


# arrays (list)
arr = [1, 2, 3]
print(arr)

# can be used as stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7) # O(n)
print(arr)

arr[0] = 0
arr[3] = 0 # O(1)


n = 5
arr = [1] * n
print(arr)
print(len(arr))



# sublist (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# similar to forloop range, last index is exclusive
print(arr[0:4])


# unpacking
a, b, c = [1, 2, 3]
print(a, b, c)



# loop through arrays
nums = [1, 2, 3]

# using index
for i in range(len(nums)):
    print(nums[i])

# without index
for n in nums:
    print(n)
    
# with index and number
for i, n in enumerate(nums):
    print(i, n)


# loops through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)



# reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)


# sorting
arr = [5, 4, 7, 3, 8]
arr.sort() # in-place
print(arr)

arr.sort(reverse=True)
print(arr)

# sort by alphabetical order by default
arr = ['bob', 'alice', 'jane', 'doe']
arr.sort()
print(arr)

# custom sort by length
arr.sort(key=lambda x: len(x))
print(arr)


# list comprehension
arr = [i + i for i in range(5)]
print(arr)


# 2-d list
arr = [[0] * 4 for i in range(4)] # [[0]*4]]*4 will not work
print(arr)


# Strings are similar to arrays
s = 'abc'
print(s[0:2])

# But string are immutable
# s[0] = 'A' # cannot do it

# so this update = create a new string
s += 'def'
print(s)


# valid numeric strings can be converted
print(int('123') + int('123'))

# and numbers can be converted to strings
print(str(123) + str(123))

# in rare case you may need ascii value of a char
print(ord('a'))
print(ord('b'))



# combine a list of strings (with an empty string 
# delimiter)
strings = ['ab', 'cd', 'ef']
print(' '.join(strings))
'''

# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft() # O(1)
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)



    
    
