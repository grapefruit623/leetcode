import unittest

class Solution:
    def isValid(self, s:str)->bool:
        rightParenthes = { ')':'(', ']':'[', '}':'{' }
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif stack != [] and rightParenthes[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if stack == [] else False


class Unittest_isValid(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = '()'
        self.assertEqual(True, self.sol.isValid(data))

    def test_sample2(self):
        data = '([)]'
        self.assertEqual(False, self.sol.isValid(data))

    def test_sample3(self):
        data = '{[]}'
        self.assertEqual(True, self.sol.isValid(data))

    def test_sample4(self):
        data = '(]'
        self.assertEqual(False, self.sol.isValid(data))

    def test_sample5(self):
        data = '({['
        self.assertEqual(False, self.sol.isValid(data))

    def test_sample6(self):
        data = ']'
        self.assertEqual(False, self.sol.isValid(data))

if __name__ == '__main__':
    unittest.main()
