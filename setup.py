# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:36:14 2020

@author: Abhilash
"""


from distutils.core import setup
setup(
  name = 'BERTSimilarity',         
  packages = ['BERTSimilarity'],   
  version = '0.1',       
  license='MIT',        
  description = 'A BERT embedding library for sentence semantic similarity measurement.',   
  long_description='This is a sentence similarity measurement library using the forward pass of the BERT (bert-base-uncased) model. The spatial distance is computed using the cosine value between 2 semantic embedding vectors in low dimensional space. These vectors can be extracted by unique words as well as the sentence as a whole.The library also provides a flexibility for choosing any other approximators for spatial distance measurement for semantic similarity measurement.References include the BERT paper(https://arxiv.org/abs/1810.04805),Google Research BERT (https://github.com/google-research/bert/)',
  author = 'ABHILASH MAJUMDER',
  author_email = 'debabhi1396@gmail.com',
  url = 'https://github.com/abhilash1910/BERTSimilarity',   
  download_url = 'https://github.com/abhilash1910/BERTSimilarity/archive/v_01.tar.gz',    
  keywords = ['Semantic Similarity','BERT','BERT Embeddings','BERT Transformer','Cosine Distance','Pytorch'],   
  install_requires=[           

          'numpy',         
          'torch',
          'transformers',
          'scipy',
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',

    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
