def continuous_subarray_sum(nums, k):
    # return True if there exists a continuous subarray of at least size 2 whose sum is a multiple of k
    # otherwise return False
    prefix_sum_modulo_k = {} # prefix sums modulo k value and index

    for i, x in enumerate(nums):
        if prefix_sum_modulo_k.get((x % k), 0) > 0:
            if prefix_sum_modulo_k.get(x % k) - i >= 2:
                return True
            else:
                prefix_sum_modulo_k[x % k] = i
    return False