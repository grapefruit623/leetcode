# -*- coding: utf-8 -*-


class fastSolution(object):

    '''
        lookup table version
    '''
    def __init__(self):
        self.grids = []
        for i in range(0, 99):
            self.grids.append([0]*99 + [1])
        self.grids.append([1]*100)

        for r in range(98, -1, -1):
            for c in range(98, -1, -1):
                self.grids[r][c] += self.grids[r+1][c] + self.grids[r][c+1]

    def printGrid(self):
        for i in self.grids:
            print (i)

    def uniquePaths(self, m, n):
        m -= 1  # for maping to array index
        n -= 1  # for maping to array index

        return self.grids[9-m][9-n]


class Solution(object):

    def checkBound(self, r, c):
        if c+1 > self.n:
            return 1
        elif r+1 > self.m:
            return 2
        else:
            return 0

    def uniquePaths(self, m, n):
        """
            type m: int
            type n: int
            rtype: int
            m by n matrix
        """
        self.grids = []
        for r in range(m):
            self.grids.append([0]*n)

        self.m = m-1
        self.n = n-1

        '''
            The element contained in grids is
            how many ways to destination
        '''
        '''
            Why self.grids[0][2] == 1 ???
            Python's bug??
        '''
        self.grids[self.m][self.n] = 1  # Finish
        self.grids[0][2] = 0  # Finish

        rows = range(self.m, -1, -1)
        cols = range(self.n, -1, -1)

        for r in rows:
            for c in cols:
                bound = self.checkBound(r, c)
                if not (r == self.m and c == self.n):  # destination point
                    if bound == 1:
                        self.grids[r][c] += self.grids[r+1][c]
                    elif bound == 2:
                        self.grids[r][c] += self.grids[r][c+1]
                    else:
                        self.grids[r][c] += self.grids[r][c+1]
                        self.grids[r][c] += self.grids[r+1][c]
        return self.grids[0][0]

if __name__ == '__main__':
    ss = fastSolution()
    ss.printGrid()
