# list.sort() sorts the list in place, return None, and only works on lists

# sorted() returns a new sorted list, leaves the original unchanged, and works on any iterable

nums = [3, 1, 2]

nums.sort() # nums is now [1, 2, 3]; return None
new = sorted(nums) # new is [1, 2, 3]; nums remains [1, 2, 3]

# Common mistakes
x = nums.sort() # Common mistake: x will be None, not the sorted list

# sorted() works on any interable
sorted("cab") # returns ['a', 'b', 'c']
print(sorted({3: "a", 2: "b", 1: "c"})) # returns [1, 2, 3]
print(sorted((3, 2, 1))) # returns [1, 2, 3]

# Sort tuples or objects by a field
people = [("Peter", 23), ("Anna", 30), ("Long", 25)]
people.sort(key=lambda p: p[1])         # by age
print(people) # [('Peter', 23), ('Anna', 30)]
