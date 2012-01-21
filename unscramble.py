#!/usr/bin/python
'''
unscramble.py - program to unscramble letters and form words. 
                Can be used when playing scrabble type games

@author: Jason Dsouza
'''

import sys
import getopt
import trie
import itertools

__author__ = ('jasonrdsouza (Jason Dsouza)')


def makeTrie():
    '''
    Function to generate the word trie. The trie consists of
    all the words in a dictionary file. Thus, the key and value 
    are both the same dictionary word. This makes searching for
    words based on prefixes efficient.
    '''
    dictionaryTrie = trie.Trie()
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            dictionaryTrie.add(line, line)
    return dictionaryTrie

def combinations(letters):
    '''
    Function to generate all possible combinations of the input
    letters, and return a list of these combinations
    '''
    combinations_list = []
    combinations_gen = itertools.permutations(letters, len(letters))
    #iterate over the generator
    for result in combinations_gen:
        temp_str = ''
        for letter in result:
            temp_str = temp_str + letter
        combinations_list.append(temp_str)
    #remove duplicates
    combinations_list = list(set(combinations_list))
    return combinations_list

def checkWords(word_trie, combination_list, full):
    '''
    Function to check the generated letter combinations against
    the word dictionary stored in a trie, and return those
    combinations that are actual words. 
    -word_trie is the dictionary trie
    -combination_list is the list of letter combinations
    -full is a boolean, true if all letters must be used
    '''
    unscrambled_list = []
    for potential_word in combination_list:
        if full:
            dictionary_word = word_trie.find(potential_word)
        else:
            dictionary_word = word_trie.find_prefix(potential_word)
        if dictionary_word != None:
            unscrambled_list.append(dictionary_word)
    unscrambled_list = list(set(unscrambled_list))
    return unscrambled_list

def sortListByLength(result_list):
    '''
    Helper function to sort the result list based on the length
    of the word, since longer words are usually better
    '''
    sorted_list = sorted(result_list, key=len)
    sorted_list.reverse()
    return sorted_list

def main(word_trie):
    '''
    Command line interface to unscramble program. Takes as input
    a trie with all the dictionary words in it.
    '''
    # Parse command line options (if present)
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['letters=', 'full', 'help'])
    except getopt.error, msg:
        usage()
        print 'Error:', str(msg)
        sys.exit(2)
    letters = ''
    full = False
    
    # Process options
    for option, arg in opts:
        if option == '--letters':
            letters = arg
        elif option == '--full':
            full = True
        elif option == '--help':
            usage()
        else:
            assert False, "unhandled option"
    
    # Perform unscrambling
    while True:
        while letters == '':
            letters = raw_input("Scrambled Letters: ")
        letter_combinations = combinations(letters)
        unscrambled_list = checkWords(word_trie, letter_combinations, full)
        result = sortListByLength(unscrambled_list)
        print result
        letters = ''


# Boilerplate code to get the program to run from the command line
if __name__ == '__main__':
  t = makeTrie()
  main(t)
