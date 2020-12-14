# BERTSimilarity

## A BERT Embedding library for sentence semantic similarity measurement :robot:

This library is a sentence semantic measurement tool based on BERT Embeddings. It uses the forward pass of the BERT (bert-base-uncased) model for estimating the embedding vectors and then applies the generic cosine formulation for distance measurement. The distance metric can be changed and the intermediate sentence and word embedding vectors can be attained as well. The model has been abstracted from the Google Research's [BERT implementation](https://github.com/google-research/bert/).The pytorch wrapper over BERT is credited to Chris McCormick.


## Dependencies

<a href="https://pytorch.org/">Pytorch</a>


<a href="https://huggingface.co/transformers/">Transformers</a>


<a href="https://www.scipy.org/">Scipy</a>


## Usability

Installation is carried out using the pip command as follows:

```python
pip install BERTSimilarity==0.1
```

For using inside the Jupyter Notebook or Python IDE:

```python
import BERTSimilarity.BERTSimilarity as bertsimilarity
```

The  'Similarity_Test.py' file contains an example of using the Library in this context.

## Samples

A sample of semantic similarity measurement with 4 different sentences , 2 of which are vaguely similar is provided below:

<img src='https://github.com/abhilash1910/BERTSimilarity/blob/master/Sample_Similarity.PNG'>

This [Colab Notebook](https://colab.research.google.com/drive/1OfFYGRdW3I8cMxL6Nj4KZd78PoiR4Lg0?usp=sharing) can be used as well for experimentation. 

A Kaggle Kernel for [Question Pair Similarity](https://www.kaggle.com/abhilash1910/bertsimilarity-library) detection is also provided which uses this library.

The Notebook is featured in [QuantumStat.com](https://notebooks.quantumstat.com/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
