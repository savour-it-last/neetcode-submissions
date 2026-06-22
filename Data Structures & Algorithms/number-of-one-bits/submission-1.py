class Solution:
    def hammingWeight(self, n: int) -> int:
        #intuitive version
        count = 0
        while n:
            # number & operation with 0000001. Its 1 if last digit is 1.
            count+=n&1
            # moves to next bit to right so 1101 becomes 110
            n>>=1
        return count