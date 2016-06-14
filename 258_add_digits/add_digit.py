import sys

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            tmp = num % 9
            if tmp == 0:
                return 9
            else:
                return tmp

if __name__ == "__main__":
    print(Solution().addDigits(int(sys.argv[1])))