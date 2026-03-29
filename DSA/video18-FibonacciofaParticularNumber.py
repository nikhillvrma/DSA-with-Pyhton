class Solution:
    def func(self, n):
        if n == 0 or n == 1:
            return n
        return self.func(n-1)+self.func(n-2)
    
    def fib(self, n):
        ans = self.func(n)
        return ans

n = int(input("Enter the Number : "))
obj = Solution()
r = obj.fib(n)
print(r)