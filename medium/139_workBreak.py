# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    '''
        Travel and prune
        AC
    '''
    def wordBreak(self, s: str, wordDict: List[str])->bool:
        l = len(s)
        self.dp = []
        for d in range(l):
            self.dp.append([False]*l)

        for i in range(0, l):
            for j in range(i, l):
                if s[i:j+1] in wordDict:
                    self.dp[i][j] = True
        j = 0
        stack = []
        while j < l:
            if self.dp[0][j] == True:
                stack.append((0,j))
            j += 1

        while stack != []:
            currentRow, currentCol = stack.pop()

            if currentCol == l-1:
                return True

            nextRow = nextCol = currentCol+1

            for j in range(nextCol, l):
                if j == l-1:
                    if self.dp[nextRow][j] == True:
                        return True
                    else:
                        self.dp[currentRow][currentCol] = False
                else:
                    if self.dp[nextRow][j] == True:
                        stack.append( (nextRow, j) )

        return False

    '''
        Two pointer
        WA
    '''
    def wordBreak_WA(self, s: str, wordDict: List[str])->bool:
        wordDict = sorted(wordDict, key=lambda x:len(x))

        i = j = 0
        maxLen = len(wordDict[-1])
        sLen = len(s)

        while i < sLen and j < sLen:
            if j-i+1 > maxLen:
                return False
            else:
                print (s[i:j+1])
                if s[i:j+1] in wordDict:
                    i = j = j+1
                else:
                    j += 1

        # The last substring happenes in wordDict
        if i == j:
            return True

        # Check the remaining substring
        # j == sLen and i < j
        if s[i:j] in wordDict:
            return True
        else:
            return False

    '''
        Recursive
        TLE
    '''
    def wordBreak_rec(self, s: str, wordDict: List[str])->bool:
        l = len(s)
        self.dp = []
        for d in range(l):
            self.dp.append([False]*l)

        for i in range(0, l):
            for j in range(i, l):
                if s[i:j+1] in wordDict:
                    self.dp[i][j] = True

        return self.recWordBreak(s, wordDict, 0, 0)

    def recWordBreak(self, s, wd, i, j):
        if i >= len(s) or j >= len(s):
            return True

        for j in range(i, len(s)):
            if self.dp[i][j] == True:
                remain = self.recWordBreak(s, wd, j+1, j+1)
                if remain == True:
                    return True

        return False

class unittest_wordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_special(self):
        s = 'a'
        wordDict = ['a']
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_special(self):
        s = 'abc'
        wordDict = ['a', 'b', 'bc']
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample1(self):
        s = "leetcode"
        wordDict = {"leet", "code"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))
    
    def test_sample2(self):
        s = "applepenapple"
        wordDict = {"apple", "pen"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample3(self):
        s = "catsandog"
        wordDict = {"cats", "dop", "sand", "and", "cat"}
        expected = False
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_TLE(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        expected = False
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_wa(self):
        s = "aaaaaaa"
        wordDict = {"aaaa", "aaa"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_wa2(self):
        s = "dogs"
        wordDict = {"dog", "s", "gs"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_wa3(self):
        s = "bccdbacdbdacddabbaaaadababadad"
        wordDict = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample_wa4(self):
        s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
        wordDict = ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl","lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi","gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc","liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn","gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog","cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck","ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi","enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh","bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj","hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac","cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda","de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb","aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj","maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc","kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki","ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e","hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb","leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem","mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei","ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb","elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo","bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk","hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf","gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk","kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad","hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm","fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg","ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh","ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee","fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln","cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb","maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o","joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib","nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni","jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc","hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj","hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom","mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj","ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil","bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an","ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma","njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna","lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl","dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe","dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk","ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn","naedmco","iohchafbega","kjejfhbco","anlhhhhg"]
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

if __name__ == "__main__":
    unittest.main()
