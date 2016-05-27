import sys
class Solution(object):
    def countBits(self, num):
        res = []
        for i in range(num+1):
            power_of_2 = len(bin(i)[2:])-1
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            else:
                res.append(res[i-2**power_of_2]+1)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(int(sys.argv[1])))