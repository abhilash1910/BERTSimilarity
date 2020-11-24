# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:43:41 2020

@author: Abhilash
"""

import BERTSimilarity as bs

'''
This is a sample example of checking similarity between 2 sentences.
This takes as inputs 2 sentences (strings).
The BERTSimilarity() class is instantiated and then the calculate_distance() method
is called, which computes the distance (cosine).
'''

if __name__=='__main__':
    f4='The Pacific Ocean is deeper than the Atlantic Ocean'
    f5='The Atlantic Ocean is smaller than the Pacific Ocean'
    bs=bs.BERTSimilarity()
    dist=bs.calculate_distance(f5,f4)
    print(dist)