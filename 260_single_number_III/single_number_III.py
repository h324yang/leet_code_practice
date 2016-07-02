class Solution(object):
    def singleNumber(self, nums):
        res = 0
        g1 = 0
        g2 = 0
        for num in nums:
            res = res ^ num
        first_diff_bit = &(res-1)
        for num in nums:
            if first_diff_bit & num == first_diff_bit:
                g1 = g1 ^ num
            else:
                g2 = g2 ^ num
        return  [g1, g2]

if __name__ == "__main__":
    nums = [1,2,1,-1,2,-1,-3,5]
    print(Solution().singleNumber(nums))
