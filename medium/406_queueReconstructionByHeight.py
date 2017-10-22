# -*- coding: utf-8 -*-
from operator import itemgetter

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        while people != []:
            height = max(people)
            tempMaxs = sorted([ k for k in people if k[0] == height[0] ])

            for t in tempMaxs:
                ans.insert(t[1], t)

            for t in tempMaxs:
                people.remove(t)

        return ans 

    def createStack(self, people):
        stack = []
        ans = []

        people.sort(key=lambda x:x[1])
        print (people)
        for i in range(0, len(people)):
            if (stack == []):
                stack.append(people[i])
            else:
                while ( len(stack) != 0 and stack[len(stack)-1][0] > people[i][0]):
                    stack.append(people[i])
                
        print ("ans: ", ans)
        print ("stack: ", stack)
        return ans

    def test(self):
        people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # people = [[9,0], [7,0], [1,9], [3,0], [2,7], [5,3], [6,0], [3,4], [6,2], [5,2]]
        ans = self.reconstructQueue(people)
        print (ans)

if __name__ == '__main__':
    sol = Solution()
    sol.test()
