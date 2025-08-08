# Nodes in a Subtree
# You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
# You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
# Signature
# int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
# Input
# A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
# Constraints
# N and Q are the integers between 1 and 1,000,000
# u is a unique integer between 1 and N
# s is of the length of N, containing only lowercase letters
# c is a lowercase letter contained in string s
# Node 1 is the root of the tree
# Output
# An integer array containing the response to each query
# Example
#         1(a)
#         /   \
#       2(b)  3(a)
# s = "aba"
# RootNode = 1
# queries = [[1, 'a']]
# Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
# output = [2]
# Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.


import math
# Add any extra import statements you may need here

class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

# Add any helper functions you may need here

## initial brute force implementation
# def find_node(root, u):
#     if root is None:
#         return None
#
#     if root.val == u:
#         return root
#
#     for child in root.children:
#         result = find_node(child, u)
#         if result is not None:
#             return result
#     return None


def preprocess_tree(root, s, frequency_map):
    if root is None:
        return [0]*26

    counts = [0] * 26

    c = s[root.val-1]
    index = ord(c) - ord('a')
    counts[index] += 1

    for child in root.children:
        child_counts = preprocess_tree(child, s, frequency_map)
        for i in range(26):
            counts[i] += child_counts[i]

    frequency_map[root.val] = counts
    return counts


def count_of_nodes(root, queries, s):
    # Write your code here

    ## initial brute force implementation
    # def count_chars(node, c):
    #     count = 0
    #
    #     if node is None:
    #         return 0
    #
    #     if s[node.val - 1] == c:
    #         count += 1
    #
    #     for child in node.children:
    #         count += count_chars(child, c)
    #
    #     return count

    frequency_map = {}
    # key - root.val, counts - array of size 26 with frequency count per char a-z indexed at 0

    preprocess_tree(root, s, frequency_map)

    result = []
    for q in queries:
        #    node = find_node(root, q[0])
        #    count = count_chars(node, q[1])
        count = frequency_map[q[0]][ord(q[1]) - ord('a')]
        result.append(count)

    return result





# TEST
root = Node(1)
child1 = Node(2)
child2 = Node(3)
root.children = [child1, child2]

# String and queries
s = "aba"
queries = [[1, 'a']]

# Call the function
print(count_of_nodes(root, queries, s))  # Expected: [2]

# Build the tree
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

root.children = [node2, node3, node4]
node3.children = [node5]

s = "abaca"
queries = [[1, 'a'], [3, 'a'], [3, 'c'], [4, 'c']]

print(count_of_nodes(root, queries, s))  # Expected: [3, 2, 0, 1]