# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]])->bool:
        visited = set()
        visited.add(0)
        # return self.traverseRooms(visited, rooms, 0)
        return self.stackSolution(visited, rooms)

    '''
        AC
        Use stack to implement DFS
    '''
    def stackSolution(self, visited, rooms):
        stack = [0]

        while stack != []:
            currentRoom = stack.pop()
            for nextRoom in rooms[currentRoom]:
                if nextRoom not in visited:
                    visited.add(nextRoom)
                    stack.append(nextRoom)

        return len(visited) == len(rooms)
    '''
        AC
        Recursion and Backtracking
    '''
    def traverseRooms(self, visited, rooms, currentRoom)->bool:
        if len(visited) == len(rooms):
            return True
        else:
            for i in rooms[currentRoom]:
                if i not in visited:
                    visited.add(i)
                    result = self.traverseRooms(visited, rooms, i)
                    if result == True:
                        return True
            return False


class Unittest_canVisitAllRooms(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        rooms = [[1], [2], [3], []]
        expected = True
        self.assertEqual(expected, self.sol.canVisitAllRooms(rooms))

    def test_sample2(self):
        rooms = [[1,3], [3,0,1], [2], [0]]
        expected = False
        self.assertEqual(expected, self.sol.canVisitAllRooms(rooms))

    def test_sample3(self):
        rooms = [[2,3], [], [2], [1,3,1]]
        expected = True
        self.assertEqual(expected, self.sol.canVisitAllRooms(rooms))

if __name__ == '__main__':
    unittest.main()
