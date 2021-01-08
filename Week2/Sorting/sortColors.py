def sortColors(nums):
    red_count = 0
    white_count = 0
    blue_count = 0

    left = 0
    right = len(nums)-1
    current = 0

    while current <= right:
        if nums[current] == 0:
            nums[left],nums[current] = nums[current],nums[left]
            left += 1

        elif nums[current] == 2:
            nums[right],nums[current] = nums[current], nums[right]
            right -= 1

        current += 1

    print(nums)


sortColors([2,0,2,1,1,0])

