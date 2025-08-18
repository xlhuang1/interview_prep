# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

def product_of_others(nums):
    prod = 1
    count_of_zeros = 0
    idx_of_zero = None

    for i, x in enumerate(nums):
        if x != 0:
            prod *= x
        else:
            count_of_zeros += 1
            idx_of_zero = i

    output = [0] * len(nums)

    if count_of_zeros > 1:
        # edge case - output all 0s
        pass
    elif count_of_zeros == 1:
        # edge case - all entries except for zero are zeros
        output[idx_of_zero] = prod
    else:
        for i, x in enumerate(nums):
            output[i] = prod//x

    return output

print(product_of_others([1, 2, 3, 4, 5]))