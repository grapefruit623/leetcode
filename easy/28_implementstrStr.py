import math
#! -*- coding: utf-8 -*-
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    '''
        2017/12/30
            WA
            haystack: mississippi
            needle: issip

        2017/12/31
            TLE
    '''
    def mystrStr(self, haystack, needle):
        if needle == "":
            return 0

        firstN = needle[0]
        needleLen = len(needle)
        needleRange = range(len(needle))

        hayStackLen = len(haystack)
        hayStackRange = range(len(haystack))
        i = 0

        stack = []

        while i < hayStackLen:
            if haystack[i] == needle[0]:
                stack.append(i)
            i += 1

        
        for i in stack:
            for j in needleRange:
                if i+j > hayStackLen-1 or haystack[i+j] != needle[j]:
                    break
            else:
                return i

        return -1
    
    '''
        2018/2/4

        TLE: 73/74 testcase
        a very long testcase make me TLE.

    '''
    def mystrStr2(self, haystack, needle):
        i = 0
        j = 0
        shift = 0
        nextIndex = 0

        if haystack == "" and needle == "":
            return 0
        while i < len(haystack):
            shift = 0
            nextIndex = 0
            j = 0
            while j < len(needle):
                if i+j < len(haystack) and haystack[i+j] == needle[j]:
                    j += 1
                    if i+j < len(haystack) and haystack[i+j] == needle[shift]:
                        if shift == 0:
                            nextIndex = i+j
                        shift += 1
                else:
                    break
            else:
                return i

            if shift == 0:
                i += 1
            else:
                i = nextIndex

        return -1 

    '''
        2018/3/25
        KMP algorithm
        How to create missMatchTable
        Table definition is from
            https://stackoverflow.com/questions/16125544/kmp-failure-function-calculation

        WA
    '''
    def mystrStr3(self, haystack, needle):

        if haystack == "" and needle == "":
            return 0

        missMatchTable = [0]*len(needle)

        '''
            Create a missMatchTable
        '''
        last = len(needle)-1

        while last > 0:
            shift = last - int(math.floor(last/2))
            while shift < last:
                i = 0
                while (i+shift) < last and needle[i] == needle[i+shift]:
                    i += 1
                else:
                    if i+shift == last: # Find pattern
                        missMatchTable[last] = i
                        break
                shift += 1

            last -= 1

        print (missMatchTable)
        '''
            Compare string
        '''
        i = 0
        while i < len(haystack):
            j = 0
            while j < len(needle):
                if i+j < len(haystack) and  haystack[i+j] == needle[j]:
                    print ('i',i,'j',j)
                    j += 1
                else:
                    if (j - missMatchTable[j] != 0):
                        i += (j - missMatchTable[j])
                    else:
                        i += 1
                    break
            else:
                return i

        return -1

    '''
        definition of missmatchTable is comes from
        http://www.csie.ntnu.edu.tw/~u91029/StringSearching.html
    '''
    def createMissmatchTable(self, arr):
        missmatchTable = [-1]*len(arr)

        if len(arr) == 1:
            missmatchTable[0] = 0
            return missmatchTable

        end = 1

        while end < len(arr):
            if arr[ missmatchTable[end-1]+1 ] == arr[end]:
                missmatchTable[end] = missmatchTable[end-1]+1
                
            end += 1

        return missmatchTable

    '''
        4th algorithm implement
        2018/05/06
        AC
    '''
    def mystrStr4(self, haystack, needle):
        '''
            Create mismatchTable
        '''
        print ("haystack: " + haystack)
        print ("needle: " + needle)

        if haystack == "" and needle == "":
            return 0 

        missmatchTable = self.createMissmatchTable(needle)
        print ("missmatchTable: ",  missmatchTable)

        i = 0
        while i < len(haystack):
            j = 0
            while j < len(needle):
                if i+j >= len(haystack):
                    return -1

                if haystack[i+j] == needle[j]:
                    j += 1 # continue to comparing
                else:
                    if j-1 < 0 or missmatchTable[j-1] == -1:
                        i += 1
                    else:
                        i += j-1- missmatchTable[j-1]

                    break
            else:
                return i 

        return -1 



def test():
    #h = "aaaaaaaaaa"
    #n = "ababc"
    #n = "aaaab"
    #h = 'mississippi'
    #n = 'issip'
    #h = "hello"
    #n = "ll"
    #h = "aaaaa"
    #n = "bba"
    #h = "aaa"
    #n = "aaaa"
    #h = ""
    #n = ""

    h = "abbabaaaabbbaabaabaabbbaaabaaaaaabbbabbaabbabaabbabaaaaababbabbaaaaabbbbaaabbaaabbbbabbbbaaabbaaaaababbaababbabaaabaabbbbbbbaabaabaabbbbababbbababbaaababbbabaabbaaabbbba"
    n = "bbbbbbaa"

    sol = Solution()
    print ('---algorithm 1---')
    print (sol.mystrStr(h, n))

    print ('---algorithm 4---')
    print (sol.mystrStr4(h, n))

if __name__ == '__main__':
    test()
