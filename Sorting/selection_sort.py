from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    # SELECTION SORT
    # SELECT  the min item to move to the SORTED part
    return unsorted_list
    
if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    sorted_list = sort_list(unsorted_list)
    print(''.join(map(str, sorted_list)))