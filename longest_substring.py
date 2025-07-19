def find_longest_substring(array):

    largest_set = {}
    window_start = 0
    window_end = 0
    at_end = False
    while at_end == False:
        char_set = {}
        for i, x in enumerate(array[window_start:]):
            window_end += 1
            if x not in char_set:
                char_set.add(x)
            else:
                window_start += 1
                if len(char_set) > len(largest_set):
                    largest_set = char_set
            if window_end == i:
                at_end = True
