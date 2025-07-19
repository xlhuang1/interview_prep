def generate_anagram_tuple(str):
    char_hash = {}
    for char in str:
        if char_hash.get(char) is not None:
            char_hash[char] = char_hash.get(char) + 1
        else:
            char_hash[char] = 1
    return tuple(sorted(char_hash.items()))

def find_string_anagrams(string_array):
    # hash of strings with the key as tuple
    hash_of_strings = {}

    for str in string_array:
        anagram_tuple = generate_anagram_tuple(str)
        if anagram_tuple in hash_of_strings:
            hash_of_strings[anagram_tuple].append(str)
        else: # add the tuple to hash and add list with str as value
            hash_of_strings[anagram_tuple] = [str]

    return list(hash_of_strings.values())

print(find_string_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))