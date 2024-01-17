from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    # INSERTION SORT
    # for each element, compare it with the previous one and then swap
    # INSERT current element to SORTED part
    # E.g. [5, 3, 2, 1]
    n = len(unsorted_list)
    for i in range(n):
        current = i
        while (current > 0 and unsorted_list[current] < unsorted_list[current-1]):
            unsorted_list[current], unsorted_list[current-1] = unsorted_list[current-1], unsorted_list[current]
            current -= 1
        
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))