
def search(nums: [int], target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Taking input
n = int(input())
nums = list(map(int, input().split()))
target = int(input())

# Calling function
result = search(nums, target)

print(result)
