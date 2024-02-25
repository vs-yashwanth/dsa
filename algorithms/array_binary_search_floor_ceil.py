
def ceiling(nums, target):  # smallest number >= target

    left = 0
    right = len(nums)-1

    while left < right:
        mid = left + (right - left)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    if nums[left] < target:
        return -1

    return nums[left], left


def floor(nums, target):  # largest number <= target

    left = 0
    right = len(nums)-1

    while left < right:
        mid = left + (right - left + 1)//2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    if nums[left] > target:
        return -1

    return nums[left], left


if __name__ == '__main__':

    print(ceiling([4, 6, 10], 6))
    print(ceiling([1, 3, 8, 10, 15], 12))
    print(ceiling([4, 6, 10], 17))
    print(ceiling([4, 6, 10], -1))

    print()

    print(floor([4, 6, 10], 6))
    print(floor([1, 3, 8, 10, 15], 12))
    print(floor([4, 6, 10], 17))
    print(floor([4, 6, 10], -1))
