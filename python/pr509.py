class Solution:
    def fib(self, n: int) -> int:
        self.map = {}
        return self.fibr(n)
        
    def fibr(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if not self.map.get(n):
            self.map[n] = self.fib(n-1) + self.fib(n-2)
        return self.map[n]
