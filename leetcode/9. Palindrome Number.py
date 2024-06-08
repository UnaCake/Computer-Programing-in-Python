class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return false

        origin = x
        store = 0 

        while x > 0:
            value = x % 10
            store = store * 10 + value
            x //= 10

        return original == store