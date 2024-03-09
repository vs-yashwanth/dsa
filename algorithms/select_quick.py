import random


def kth_smallest(nums, k):
    return quick_select(nums, 0, len(nums)-1, k)


def quick_select(nums, left, right, k):
    if left <= right:
        pivot = rand_partition(nums, left, right)
        cur = pivot - left + 1
        if cur == k:
            return nums[pivot]
        elif cur > k:
            return quick_select(nums, left, pivot-1, k)
        else:
            return quick_select(nums, pivot+1, right, k-cur)


def rand_partition(nums, left, right):
    pivot = right
    rand = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    return partition(nums, left, right)


def partition(nums, left, right):
    pivot = nums[right]
    i = j = left
    while i < right:
        if nums[i] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    nums[j], nums[right] = nums[right], nums[j]
    return j


if __name__ == '__main__':

    print(kth_smallest([3, 2, 1, 5, 6, 4], 2))  # 2
    print(kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3))  # 2
