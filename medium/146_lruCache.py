# -*-coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class DLinkNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUDLinkList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentListLen = 0

        self.head = DLinkNode(-1, -1)
        self.tail = DLinkNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        # key => obj
        self.hashTable = {}

    def getNode(self, key):
        if key in self.hashTable:
            ret = self.hashTable[key].value

            tempKey, tempValue = key, ret
            self.removeNode(key)
            self.insertNode(tempKey, tempValue)

            return ret
        else:
            return -1
    
    def insertNode(self, key, value):
        if self.currentListLen == self.capacity:
            rKey = self.tail.prev.key
            self.removeNode(rKey)

        node = DLinkNode(key, value)

        self.head.next.prev = node
        node.next = self.head.next

        self.head.next =node
        node.prev = self.head

        self.hashTable[key] = node

        self.currentListLen += 1

    def updateNode(self, key, value):
        if key in self.hashTable:
            # Swap
            self.removeNode(key)
            self.insertNode(key, value)
        else:
            self.insertNode(key, value)

    def removeNode(self, key):
        if key in self.hashTable:
            node = self.hashTable[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev

            self.hashTable.pop(key)
            self.currentListLen -= 1
        else:
            return -1

'''
    ref: https://josephjsf2.github.io/data/structure/and/algorithm/2020/05/09/LRU.html
'''
class LRUCache:
    def __init__(self, capacity: int):
        self.LRUData = LRUDLinkList(capacity)

        return None

    def get(self, key: int) -> int:
        return self.LRUData.getNode(key)
        

    def put(self, key: int, value: int) -> None:
        self.LRUData.updateNode(key, value)
        return None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Unittest(unittest.TestCase):
    def setUp(self):
        pass

    def simulateLRU(self, cmd, para):
        result = []
        l = len(cmd)
        lRUCache = None

        for i in range(l):
            if cmd[i] == "LRUCache":
                self.lRUCache = LRUCache( para[i][0] )
                result.append(None)
            elif cmd[i] == "put":
                self.lRUCache.put( para[i][0], para[i][1] )
                result.append(None)
            elif cmd[i] == "get":
                r = self.lRUCache.get( para[i][0] )
                result.append(r)

        return result

    def test_case1(self):
        cmd = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        para = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        expect = [None, None, None, 1, None, -1, None, -1, 3, 4]

        result = self.simulateLRU(cmd, para)

        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
