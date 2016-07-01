from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumberTrivial(self, nums):
        first = True
        res = None
        for num in nums:
            if first == True:
                res = num
                first = False
            else:
                res = res ^ num
        return res

if __name__ == "__main__":
    data = [2,3]
    print(Solution().singleNumber(data))