nums = [2, 7, 11, 15]
target = 9
need = 0

def two_sum(nums, target):
    nums_indexes = {}

    for index, num in enumerate(nums):
        need = target - num

        if need in nums_indexes:
            return [nums_indexes[need], index]

        nums_indexes[num] = index


print(two_sum(nums, target))