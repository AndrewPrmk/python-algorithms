nums = [1, 2, 3, 1]

def contains_dublicate(nums):
    return len(nums) != len(set(nums))


print(contains_dublicate(nums))