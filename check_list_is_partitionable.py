def is_subset_exist_with_sum(arr, required_sum):
    for i in range(1, len(arr)+1):
        for perm in permutations(arr, i):
            if sum(perm) == required_sum:
                return True
    return False


def is_list_partitionable(arr):
    result = None
    size = len(arr)
    total_sum = sum(arr)
    # If sum is odd, then list cannot be partition
    if total_sum%2 == 1:
        result = False
    else:
        # Now try to find a list with half of total sum of list
        result = is_subset_exist_with_sum(arr, total_sum//2)

    print 'List: {0} is partitionable: {1}'.format(arr, result)
    return result
    
if __name__ == '__main__':
    is_list_partitionable([])
    is_list_partitionable([3, 3])
    is_list_partitionable([3, 1])
    is_list_partitionable([1, 2, 3, 1, 2, 3])
    is_list_partitionable([1, 2, 3, 5, 1])
    is_list_partitionable([5, 1, 2, 3, 1])
    is_list_partitionable([6, 9, 3])
    is_list_partitionable([6, 9, 3, 1])    
    
"""
List: [] is partitionable: False
List: [3, 3] is partitionable: True
List: [3, 1] is partitionable: False
List: [1, 2, 3, 1, 2, 3] is partitionable: True
List: [1, 2, 3, 5, 1] is partitionable: True
List: [5, 1, 2, 3, 1] is partitionable: True
List: [6, 9, 3] is partitionable: True
List: [6, 9, 3, 1] is partitionable: False


Time complexity: O(n*n!)
"""
