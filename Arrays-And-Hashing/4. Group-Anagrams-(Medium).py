"""
Problem: https://neetcode.io/problems/anagram-groups?list=neetcode150

Description:
    Given an array of strings strs, 
    group all anagrams together into 
    sublists. You may return the output 
    in any order.

    An anagram is a string that contains 
    the exact same characters as another 
    string, but the order of the characters 
    can be different.

Examples:
    Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]

        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    Example 2:
        Input: strs = ["x"]

        Output: [["x"]]

    Example 3:
        Input: strs = [""]

        Output: [[""]]
        


Recommended Time & Space Complexity:
    Time:   O(m * n)
    Space:  O(m)
"""

