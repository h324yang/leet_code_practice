class Solution(object):
    def moveZeroes(self, nums):
        zero_count = 0
        for i in range(len(nums)):
            if nums[i-zero_count] == 0:
                nums.pop(i - zero_count)
                zero_count += 1
        for i in range(zero_count):
            nums.append(0)

if __name__ == "__main__":
    nums = [1, 0, 3, 0, 10, 17, 12]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)