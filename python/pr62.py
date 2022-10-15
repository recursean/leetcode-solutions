class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {'1,1': 1}
        self.trv(m, n)
        return self.memo[f'{m},{n}']
    
    def trv(self, m, n):
        if self.memo.get(f'{m},{n}'):
            return self.memo[f'{m},{n}']
        if m == 0 or n == 0:
            return 0
        
        self.memo[f'{m},{n}'] = self.trv(m-1, n) + self.trv(m, n-1)
        return self.memo[f'{m},{n}']
