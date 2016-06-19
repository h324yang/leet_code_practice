class Solution(object):
    def intersection(self, nums1, nums2):
        dict = {}
        res = []
        for item in nums1:
            dict[item] = False
        for item in nums2:
            try:
                if dict[item] == False:
                    dict[item] = True
            except:
                pass
        for item in dict.items():
            if item[1] == True:
                res.append(item[0])
        return res

if __name__ == "__main__":
    nums1 = [1,2,3,4,5]
    nums2 = [2,1,4,10,12]
    print(Solution().intersection(nums1, nums2))