

def max_sub_array(nums):
    maxsub = nums[0]
    cursum = 0

    for i in nums:
        if cursum < 0:
            cursum = 0
        cursum += i
        maxsub = max(maxsub, cursum)
    return maxsub


if __name__ == "__main__":
    print(max_sub_array([-7, 4, 1, -11, 9, 3]))
