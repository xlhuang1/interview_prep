import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def print_a(array_a):
    for i in array_a:
        print(i)



def are_they_equal(array_a, array_b):
    # Write your code here
    array_a.sort() # sorts run in O(n log n)
    array_b.sort()
    for i, x in enumerate(array_a):
        if array_b[i] != x:
            # checks each element in the sorted arrays, if there is mismatch then we know that it cannot be made equal.
            # this runs in O(n) time
            return False
    return True











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
    print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

    # Add your own test cases here

    n_3 = 20
    a_3 = [1, 3, 2, 3, 1, 2, 3, 5, 7, 8, 1, 3, 2, 3, 1, 2, 3, 5, 7, 8]
    b_3 = [1, 2, 3, 3, 1, 1, 3, 5, 7, 8, 1, 3, 2, 3, 1, 2, 3, 5, 7, 8]
    expected_3 = False
    output_3 = are_they_equal(a_3, b_3)
    check(expected_3, output_3)

    n_4 = 20
    a_4 = [1, 3, 2, 3, 1, 2, 3, 5, 7, 8, 1, 3, 2, 3, 1, 2, 3, 5, 7, 8]
    b_4 = [1, 2, 3, 3, 3, 2, 3, 5, 7, 8, 1, 3, 2, 3, 1, 2, 1, 5, 7, 8]
    expected_4 = True
    output_4 = are_they_equal(a_4, b_4)
    check(expected_4, output_4)