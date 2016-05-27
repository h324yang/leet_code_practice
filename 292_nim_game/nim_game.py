import sys
class Solution(object):
    def canWinNim(self, n):
        if not n%4 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.canWinNim(int(sys.argv[1])))