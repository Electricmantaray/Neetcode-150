"""
Algorithm: Tim Sort

Sources:
    - https://en.wikipedia.org/wiki/Timsort

Description:
    TimSort is a derivitive hybrid of Merge Sort and
    Insertion Sort.(Used in .sort() and sorted() until
    python 3.11)

    The algorithm finds subsequences of data already
    ordered (runs) and uses them to sort the remainder
    more efficiently.

    Basically divide and conquer then use insertion sort
    on sub arrays and merge.

Examples:
    Example 1:
        Input: nums = [4, 0, 12, 35, 89, 56, 3, 30, 12, 5, 64, 55, 29, 17, 1, 2, 3, 4, 5, 33, 7, 18, 26, 51, 63, 22, 844, 91, 73, 47]

        1. 
            Run size = 4
            [4, 0, 12, 35|, 89, 56, 3, 30|, 12, 5, 64, 55|, 29, 17, 1, 2|, 3, 4, 5, 33|, 7, 18, 26, 51|, 63, 22, 84, 91|, 73, 47]
            Insertion Sorting:
                [0, 4, 12, 35],
                [3, 30, 56, 80],
                [5, 12, 55, 64],
                [1, 2, 17, 29],
                [3, 4, 5, 33],
                [7, 18, 26, 51],
                [22, 63, 84, 91],
                [47, 73]
            [0, 4, 12, 35|, 3, 30, 56, 80|, 5, 12, 55, 64|, 1, 2,17, 29|, 3, 4, 5, 33|, 7, 18, 26, 51|, 22, 63, 84, 91|, 47, 73]

        2.
            Run Size = 8
            [0, 4, 12, 35, 3, 30, 56, 80|, 5, 12, 55, 64, 1, 2,17, 29|, 3, 4, 5, 33, 7, 18, 26, 51|, 22, 63, 84, 91, 47, 73]
            Insertion Sorting:
                [0, 3, 4, 12, 30, 35, 56, 80],
                [1, 2, 5, 12, 17, 29, 55, 64],
                [3, 4, 5, 7, 18, 26, 33, 51],
                [22, 47, 63, 73, 84, 91]
            [0, 3, 4, 12, 30, 35, 56, 80|, 1, 2, 5, 12, 17, 29, 55, 64|, 3, 4, 5, 7, 18, 26, 33, 51|, 22, 47, 63, 73, 84, 91]

        3.
            Run Size = 16
            [0, 3, 4, 12, 30, 35, 56, 80, 1, 2, 5, 12, 17, 29, 55, 64|, 3, 4, 5, 7, 18, 26, 33, 51, 22, 47, 63, 73, 84, 91]
            Insertion Sorting:
                [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80],
                [3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80|, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]

        4.
            Run Size = 32
            [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            Insertion Sorting:
                [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]
        [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]


        Solved

        Output: [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]


Outcome:
    Pros:
        - Very good at sorting lists that are partially sorted
        - Stable sorting algorithm
        - Easy to understand as its a hybrid of merge and insertion

    Cons:
        - High space complexity as it is not an in-place sort
        - Slightly slower on random data as its designed for real world
        data that incudes trends or partially sorted lists


Time & Space Complexity:
    Time:
        Best:       O(n)

        Average:    O(n log(n))

        Worst:      O(n log(n))


    Space:
        Worst:      O(n)
        
"""