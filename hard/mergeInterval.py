class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str( [self.start, self.end] )

class Solution(object):

    def merge(self, intervals):
        self.llist = intervals
        self.llist = sorted(self.llist, key=lambda x:x.start)

        self.ans = []
        if [] != intervals:
            self.ans.append( self.llist[0] )
            ansIndex = 0

            for i in self.llist[1:]:
                cur = self.ans[ansIndex] 
                if cur.end >= i.start and cur.end <= i.end:
                    self.ans[ansIndex] = Interval(cur.start, i.end) 
                elif cur.end < i.start:
                    self.ans.append(i)
                    ansIndex += 1

        return self.ans


    def printLlist(self):
        for i in self.llist:
            print i,

    def printAns(self):
        for i in self.ans:
            print i,

if __name__ == '__main__':
    ss = Solution()

    l = [ [2,3], [4,6], [8,10], [5,18]]

    llist = []

    for i in l:
        llist.append(Interval(i[0], i[1]))


    ss.merge(llist)

    ss.printLlist()
    print '\n'+'='*15
    ss.printAns()
