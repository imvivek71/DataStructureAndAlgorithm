"""
The way we organize data is known as data structure.

Two types of data structures:

1). Linear data structures:

    A data structure where data elements are  sequentially or linearly arranged, where the elements
    are attached to its previous and next adjacent. In linear ds single level is involved and we can
    traverse all the elements in single run only.
    LDS is easy because computer memory is also arranged in linear wy only.

    Examples:
        1. array
        2. list
        3. stack
        4. queue
        5 linked list .etc

2). Non-Linear data structures:

    A Data structure where data elements are not sequentially or linearly arranged known as Non-Linear ds
    Single level is not involved, hence we can traverse each elements in single run only.
    It is not easy to implement & it utilizes computer memory efficiently in comparision to lds
"""


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


print(insertionSort([1, 5, 4, 3, 7, 6]))
