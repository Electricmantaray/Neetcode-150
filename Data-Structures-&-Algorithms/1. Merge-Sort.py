"""
Algorithm: Merge Sort

Description:
    The data is repeatedly split in 
    half until each item is its own list.

    Adjacent lists are then merged back
    together, with each item in the sub-list
    being entered in its correct sorted 
    position.

Examples:
    Example 1:
        Input: nums = [3, 3, 1, 5, 2, 3, 4, 4, 2]

        1. [3, 3, 1, 5, 2, 3, 4, 4, 2, 7, 1, 9]
        2. [[3, 3, 1, 5, 2, 3], [4, 4, 2, 7, 1, 9]]
        3. [[3, 3, 1], [5, 2, 3], [4, 4, 2], [7, 1, 9]]
        4. [[3], [3, 1], [5], [2, 3], [4], [4, 2], [7], [1, 9]]
        5. [[3], [3], [1], [5], [2], [3], [4], [4], [2], [7], [1], [9]]

        Every item is now its own list

        1.[[3], [3], [1], [5], [2], [3], [4], [4], [2], [7], [1], [9]]
        2.[[3, 3], [1, 5], [2, 3], [4, 4], [2, 7], [1, 9]]
        3.[[1, 3, 3, 5], [2, 3, 4, 4], [1, 2, 7, 9]]
        4.[[1, 2, 3, 3, 3, 4, 4, 5], [1, 2, 7, 9]] # Odd number of lists retains the last list
        5.[1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 9]

        Solved

        Output: [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 9]

Outcome:
    Pros:
        - Consistent Performance
        - Stable Sorting
        - Efficient for large datasets
        - Parallelisable (nature of divide and conquer)
        - Suitable for external sorting

    Cons:
        - Space Complexity high
        - Not In-Place
        - Slower for small datasetes
        - Recursive Overhead
        - Complex implimentation


Time & Space Complexity:
    Time:
        Best:    O(n log(n))

        Average: O(n log(n))

        Worst:   O(n log(n))


    Space:
        Worst:   O(n)

"""