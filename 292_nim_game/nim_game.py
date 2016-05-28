import sys
class Solution(object):
    def canWinNim(self, n):
        return not n%4 == 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.canWinNim(int(sys.argv[1])))