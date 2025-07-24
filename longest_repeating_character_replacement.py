# You are given a string s and an integer k.
# You can replace at most k characters in the string so that all characters in a windowed substring are the same.
#
# Return the length of the longest such substring.

# s = "AABABBA"
# k = 1
# Output: 4

def longest_repeating_char(k, s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    left_index = 0
    right_index = 0
    max_len = 0
    max_freq = 0
    char_freq = {}

    while right_index < len(s):
        char_freq[s[right_index]] = char_freq.get(s[right_index], 0) + 1
        max_freq = max(max_freq, max(char_freq.values()))
        window_size = right_index - left_index + 1
        if window_size - max_freq > k:
            # window invalid
            char_freq[s[left_index]] = char_freq.get(s[left_index], 0) - 1
            left_index += 1
            window_size -= 1
        max_len = max(max_len, window_size)
        right_index += 1
    return max_len



def test_longest_repeating_char():
    # Case 1: Example from the problem
    assert longest_repeating_char(1, "AABABBA") == 4  # Replace one 'B' → "AABA"

    # Case 2: All characters are the same
    assert longest_repeating_char(2, "AAAA") == 4  # Already all 'A's

    # Case 3: Replace all different characters
    assert longest_repeating_char(2, "ABCD") == 3  # Replace 2 letters → "AAA" or "BBB"

    # Case 4: Single character
    assert longest_repeating_char(5, "A") == 1  # Only 1 char

    # Case 5: Empty string
    assert longest_repeating_char(2, "") == 0  # Nothing to replace

    # Case 6: No replacements allowed (k=0)
    assert longest_repeating_char(0, "AABABBA") == 2  # Longest run of same char is "AA"

    # Case 7: Multiple possibilities
    assert longest_repeating_char(2, "AABABBAAA") == 6  # Replace Bs → "AAAAAA"

    print("All test cases passed!")

test_longest_repeating_char()