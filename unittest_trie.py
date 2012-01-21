#!/usr/bin/python
'''
unittest_trie.py - test cases for trie class

Reference: http://docs.python.org/library/unittest.html
           http://docs.python.org/release/2.5.2/lib/minimal-example.html

@author: Jason Dsouza
'''

import unittest
import trie

__author__ = ('jasonrdsouza (Jason Dsouza)')


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.t = trie.Trie()
        self.t.add("foo", "A")
        self.t.add("fo", "B")
        self.t.add("l", "C")
    
    def test_find(self):
        self.assertEqual(self.t.find("fo"), "B")
        self.assertEqual(self.t.find("fool"), None)
        self.assertEqual(self.t.find("foo"), "A")
        self.assertEqual(self.t.find("l"), "C")
        
    def test_findprefix(self):
        self.assertEqual(self.t.find_prefix("fo"), ("B", ""))
        self.assertEqual(self.t.find_prefix("fool"), ("A", "l"))
    
if __name__ == '__main__':
    unittest.main()
