# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq = {}
    t_freq = {}

    for c in s:
        s_freq[c] = s_freq.get(c, 0) + 1

    for c in t:
        t_freq[c] = t_freq.get(c, 0) + 1

    for item in s_freq.items():
        if item[1] != t_freq.get(item[0]):
            return False
    return True

print(is_anagram("racecar", "carrace"))
print(is_anagram("jar", "jam"))
print(is_anagram("aba", "abac"))