#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.endsHere = False

def noPrefix(words):
    # Write your code here
    res_word = ''
    
    #construct trie from words
    root = TrieNode('')
        
    #for each word check if there exists a prefix in trie
    for word in words:
        parent = root
        
        for i in range(len(word)):
            if word[i] not in parent.children:
                break
            
            elif word[i] in parent.children:
                parent = parent.children[word[i]]
                
                if i == len(word)-1:
                    print("BAD SET")
                    print(word)
                    return 
                
            if parent.endsHere:
                print("BAD SET")
                print(word)
                return 
        
        cur_root = parent
        
        for j in range(i,len(word)):
            if word[j] not in cur_root.children:
                cur_root.children[word[j]] = TrieNode(word[j])
                
            cur_root = cur_root.children[word[j]]
            
        cur_root.endsHere = True
    
    print("GOOD SET")


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
