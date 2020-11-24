# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:48:13 2020

@author: Abhilash
"""

import BERTSimilarity.BERTSimilarity as bertsimilarity
'''
This is a sample example of checking similarity between 2 sentences.
This takes as inputs 2 sentences (strings).
The BERTSimilarity() class is instantiated and then the calculate_distance() method
is called, which computes the distance (cosine).
'''

if __name__=='__main__':
    f1='The man is playing soccer.'
    f2='The man is playing football.'
    bertsimilarity=bertsimilarity.BERTSimilarity()
    dist=bertsimilarity.calculate_distance(f1,f2)
    print('The distance between sentence1: '+f1+' and sentence2: '+f2+' is '+str(dist))
    f1='The company forecasted a profit of 10%'
    f2='The F1 company did not loose the race in England'
    f3='The Titanic sank in the Atlantic Ocean'
    f4='The Pacific Ocean is deeper in the Atlantic Ocean'
    d1=bertsimilarity.calculate_distance(f1,f2)
    d2=bertsimilarity.calculate_distance(f1,f3)
    d3=bertsimilarity.calculate_distance(f3,f4)
    d4=bertsimilarity.calculate_distance(f1,f4)
    print('The distance between sentence1: '+f1+' and sentence2: '+f2+' is '+str(d1))
    print('The distance between sentence1: '+f1+' and sentence3: '+f3+' is '+str(d2))
    print('The distance between sentence3: '+f3+' and sentence4: '+f4+' is '+str(d3))
    print('The distance between sentence1: '+f1+' and sentence4: '+f4+' is '+str(d4))