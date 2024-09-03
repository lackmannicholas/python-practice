from typing import List

# Runtime: Big O(N) by iterating through all the items in the list
# Memory: Big O(1) implemented filtering in-place by replacing the existing list with arr[:] rather than arr
def moveZerosToEnd(arr: List[int]) -> List[int]:
    # short circuit based on edge-case
    if len(arr) < 2:
        return arr
    
    # filter lists by removing zeros
    initial_length = len(arr)
    arr[:] = [item for item in arr if not item == 0]
    filtered_length = len(arr)

    # re-add zeros with the difference between the initial and filtered lengths
    while filtered_length < initial_length:
        arr.append(0)
        filtered_length += 1
    
    return arr

    
# debug your code below
print(moveZerosToEnd([0, 1, 0, 3, 12]))