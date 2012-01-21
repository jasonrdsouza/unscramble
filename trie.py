'''
trie.py - Python implementation of a trie datastructure

Reference: http://jtauber.com/2005/02/trie.py
           http://en.wikipedia.org/wiki/Trie

@author: Jason Dsouza
'''

__author__ = ('jasonrdsouza (Jason Dsouza)')


class Trie:
    '''
    A trie is essentially a tree structure, where the position
    of a node is determined by traversal based on the key 
    (usually a string). Due to this, it allows look up based on
    the longest prefix that matches.
    '''
    
    def __init__(self):
        self.root = [None, {}]
    
    def add(self, key, value):
        '''
        Add the given value for the given key to the trie
        '''
        curr_node = self.root
        for ch in key:
            curr_node = curr_node[1].setdefault(ch, [None, {}])
        curr_node[0] = value
    
    def find(self, key):
        '''
        Return the value for the given key, or None if key 
        not found
        '''
        curr_node = self.root
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                return None
        return curr_node[0]
        
    def find_prefix(self, key):
        '''
        Find as much of the key as you can, using the longest 
        prefix that has a value. Return (value, remainder) where
        remainder is the rest of the given key
        NOTE: removed the (value remainder) tuple, and replaced it
              with just the value
        '''
        curr_node = self.root
        #remainder = key
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                #return (curr_node[0], remainder)
                return curr_node[0]
            #remainder = remainder[1:]
        #return (curr_node[0], remainder)
        return curr_node[0]
        
    
