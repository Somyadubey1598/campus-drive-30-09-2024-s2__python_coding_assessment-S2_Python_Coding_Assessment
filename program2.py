class Solution(object):
    def romanToInt(self, s:str)-> int:
                   d={'I':1,'v': 5, 'X' : 10, 'L': 50, 'c':100, 'D': 500, 'M': 1000}
                      return sum ((-1 if d[a] < d[b] else 1) * d[a] for a, b in pair wise(s)) + d[s[-1]]
        



