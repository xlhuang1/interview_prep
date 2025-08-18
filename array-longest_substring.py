# Given a string s and an integer k, return the length of the longest substring that can be turned into a string of all the same character by replacing at most k characters.

# sliding window that meets constraint --> increase window size until this constraint : window_size - max_count > k

def characterReplacement(s, k):
    if not s:
        return 0

    left = 0
    right = 0
    max_count = 0

    char_freq = {i : 0 for i in range(ord('A'), ord('Z')+1)}
    for i, c in enumerate(s):
        right = i
        char_freq[ord(c)] += 1
        max_count = max(max_count, char_freq[ord(c)])

        window_size = right - left + 1
        if window_size - max_count > k:
            # shrink window and decrease freq of left
            char_freq[ord(s[left])] -= 1
            left += 1
    return right - left + 1

print(characterReplacement("AZZZZAABA", 1))