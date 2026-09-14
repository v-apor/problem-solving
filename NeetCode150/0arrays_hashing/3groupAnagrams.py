# https://leetcode.com/problems/group-anagrams/description/

# Approach:
# Let's start with first, 
# the best way to check if two elements are anagrams or not,
# is to have two arrays of size 26, count the freq of each chars
# compare it, if it doesn't match, then not an anagram
# Time O(n) | Space O(1)

# Now, we have an array of elements, worst case scenario,
# We will have to perform this operation for every single element with the other
# Time O(n^2 * m), where m is avg word len | Space O(n * m)

# Better
# If we already have the char_freq of each word, can use it as hash,
# Instead of checking all possible combinations
# Time O(n * m) | Space O(n * m)

from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    for word in strs:
        temp_list = [0] * 26
        for ch in word:
            temp_list[ord(ch) - ord('a')] += 1
        res[tuple(temp_list)].append(word)
    return list(res.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
