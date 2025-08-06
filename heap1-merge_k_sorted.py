# You're given an array of k sorted linked lists.
# Each list is sorted in ascending order.
# Goal: merge all the lists into one sorted linked list and return its head

# Input: lists = [
#   1 -> 4 -> 5,
#   1 -> 3 -> 4,
#   2 -> 6
# ]
#
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted(linked_list_array):
    if not linked_list_array:
        return None

    head = ListNode()
    result = head
    k_list_heap = []

    for i, sorted_list in enumerate(linked_list_array):
        # put all head onto min-heap
        if sorted_list:
            heapq.heappush(k_list_heap, (sorted_list.val, i, sorted_list))

    while k_list_heap:
        next_item = heapq.heappop(k_list_heap)
        # put the next item into the final sorted list
        result.next = ListNode(next_item[0])
        result = result.next

        # move to the next item in list and push back onto heap
        next_node = next_item[2].next
        if next_node is not None:
            heapq.heappush(k_list_heap, (next_node.val, next_item[1], next_node))
    return head.next