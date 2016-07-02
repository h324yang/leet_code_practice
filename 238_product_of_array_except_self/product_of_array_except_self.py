class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        left2right = 1
        right2left = 1
        for i in range(n-1):
            left2right *= nums[i]
            right2left *= nums[-(i+1)]
            res[i+1] *= left2right
            res[-(i+2)] *= right2left
        return res

if __name__ == "__main__":
    data  = [1,2,3,4]
    print(Solution().productExceptSelf(data))