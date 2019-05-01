# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    '''
        Using Dijkstra's algorithm
        TLE
    '''
    def findCheapestPrice(self, n:int, flights: List[List[int]], src:int, dst:int, k:int)->int:
        # -1 is meaning cities which can not be arrived from city n
        self.weightMatrix = [ [-1]*n for i in range(n) ]
        for f in flights:
            self.weightMatrix[ f[0] ][ f[1] ] = f[2]

        cityCost = [ [float('inf')]*n for step in range(k+1) ]
        citiesQueue = []

        '''
            price of starting city is zero and step is 0(init)
        '''

        citiesQueue.append( (src,0) ) # starting city
        cityCost[0][src] = 0 
        minCost = float('inf')

        while citiesQueue != []:
            currentCity, step = citiesQueue.pop(0)
            if step <= k:
                for city,price in enumerate(self.weightMatrix[currentCity]):
                    if price != -1:

                        currentCost = self.weightMatrix[currentCity][city]
                        if step > 0:
                            currentCost += cityCost[step-1][currentCity]  
                            if currentCost < cityCost[step][city]:
                                cityCost[step][city] = currentCost 
                        else:
                            cityCost[step][city] = currentCost

                        '''
                            Pruning
                        '''
                        if currentCost < minCost:
                            citiesQueue.append( (city, step+1) )
                    
                    if city == dst:
                        minCost = min(minCost, cityCost[step][city])
        
        return minCost if minCost != float('inf') else -1

class Unittest_findCheapestPrice(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    '''
    def test_sample1(self):
        n = 3
        edges = [[0,1,100], [1,2,100], [0,2,500]]
        src = 0
        dst = 2
        k = 1
        expected = 200
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))

    # WA sample1
    def test_sample2(self):
        n = 5
        edges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
        src = 2
        dst = 1
        k = 1
        expected = -1 
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))
    # WA sample2
    def test_sample3(self):
        n = 4
        edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
        src = 0
        dst = 3
        k = 1
        expected = 6 
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))

    # Ouput limit exceeded
    def test_sample4(self):
        n = 18
        edges = [[16,1,81],[15,13,47],[1,0,24],[5,10,21],[7,1,72],[0,4,88],[16,4,39],[9,3,25],[10,11,28],[13,8,93],[10,3,62],[14,0,38],[3,10,58],[3,12,46],[3,8,2],[10,16,27],[6,9,90],[14,8,6],[0,13,31],[6,4,65],[14,17,29],[13,17,64],[12,5,26],[12,1,9],[12,15,79],[16,11,79],[16,15,17],[4,0,21],[15,10,75],[3,17,23],[8,5,55],[9,4,19],[0,10,83],[3,7,17],[0,12,31],[11,5,34],[17,14,98],[11,14,85],[16,7,48],[12,6,86],[5,17,72],[4,12,5],[12,10,23],[3,2,31],[12,7,5],[6,13,30],[6,7,88],[2,17,88],[6,8,98],[0,7,69],[10,15,13],[16,14,24],[1,17,24],[13,9,82],[13,6,67],[15,11,72],[12,0,83],[1,4,37],[12,9,36],[9,17,81],[9,15,62],[8,15,71],[10,12,25],[7,6,23],[16,5,76],[7,17,4],[3,11,82],[2,11,71],[8,4,11],[14,10,51],[8,10,51],[4,1,57],[6,16,68],[3,9,100],[1,14,26],[10,7,14],[8,17,24],[1,11,10],[2,9,85],[9,6,49],[11,4,95]]
        src = 7
        dst = 2
        k = 6
        expected = 169 
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))
    '''

    # Time limit exceeded
    def test_sample5(self):
        n = 15
        edges = [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
        src = 1
        dst = 4
        k = 10
        expected = 169 
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))

    # WA
    def test_sample6(self):
        n = 11
        edges = [[5,7,4250],[8,4,8564],[7,9,5145],[5,6,974],[3,10,2626],[7,0,4533],[6,9,8181],[10,4,8331],[3,2,5223],[8,10,8342],[4,0,5683],[5,10,8848],[9,10,6415],[1,4,5031],[10,0,4782],[6,5,4003],[10,3,6335],[4,9,9133],[2,5,9870],[0,10,4406],[7,3,897],[9,5,8190],[7,5,9862],[2,0,2696],[7,6,9910],[0,6,3244],[0,8,3332],[1,3,4477],[8,7,9486],[6,3,246],[0,3,5373],[9,6,7210],[5,1,5804],[4,1,1434],[4,8,5625],[5,0,2894]]
        src = 4
        dst = 2
        k = 7
        expected = 11134
        self.assertEqual(expected, self.sol.findCheapestPrice(n, edges, src, dst, k))


if __name__ == "__main__":
    unittest.main()
