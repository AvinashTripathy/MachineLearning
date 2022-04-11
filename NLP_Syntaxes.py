find the most similar words in word2vec

import gensim
gensim.__version__
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
model_skip = Word2Vec.load('/model/word2vec_dec_21.model')
model_cbow = Word2Vec.load('/model/word2vec_skip_dec_21.model')
model_skip.most_similar("intellicheck", topn=10)
model_cbow.most_similar("intellicheck", topn=10)
